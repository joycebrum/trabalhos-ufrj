#Cliente - camada de interface com o cliente

import socket
import json
import ast
import select
import sys
import random
import aplication_log as log

HOST = 'localhost' 
PORTA = 5000

MYHOST = 'localhost' 
MYDOOR = int(random.uniform(5010, 7010))

BYTES_LEN = 4

username = ''
avaiable_users = {}
inputs = [sys.stdin]
chunks_rest = []

#Garante o recebimento completo do json de resposta do servidor
def recvall(sock):
    chunks = []
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            return None
        chunks.append(chunk)
        try:
            req = b''.join(chunks)
            req_json = json.loads(str(req, encoding='utf-8'))
        except: #if occurs error means that req is not the full json file
            continue
        return req_json

#Formata e envia uma requisição genérica
def send_req(server, operation, args):
    req = json.dumps({"requisition": { "operation": operation, "arguments": args}})
    server.sendall(bytes(req, encoding='utf-8')) #envia a requisicao

    return recvall(server)

#Limpa a lista de usuários ativos
def clear_avaiable_users():
    for value in list(avaiable_users.values()):
        if value['socket']:
            value['socket'].close()
    avaiable_users.clear()

#atualiza a lista de usuários disponíveis
def update_avaiable_users(users):
    #remove users that are not no longer connected
    for user in list(avaiable_users.keys()):
        if user not in users:
            if avaiable_users[user]['socket']: avaiable_users[user]['socket'].close()
            avaiable_users.pop(user, None)

    for user in users:
        if user[0] not in avaiable_users:
            avaiable_users[user[0]] = { 'endr': [user[1], user[2]], 'socket': None }
        elif user[1] != avaiable_users[user[0]]['endr'][0] or user[2] != avaiable_users[user[0]]['endr'][1]:
            if avaiable_users[user[0]]['socket']: avaiable_users[user[0]]['socket'].close()
            avaiable_users[user[0]]['endr'] = [user[1], user[2]]
            avaiable_users[user[0]]['socket'] = None

def is_valid_username(name):
    return name.isalnum()
#efetua o login no servidor, enviando o username e a porta onde aceita conexões
def login(server):
    global username
    while True:
        user_input = input()
        if user_input == 'exit': break
        if not user_input.isalnum():
            log.invalid_username()
            continue
        response = send_req(server, 'login', [user_input.strip(), MYHOST, MYDOOR])
        
        if response['response'][0] == 0:
            log.welcome(user_input)
            username = user_input.strip()
            break
        else:
            log.username_in_use()

#Busca pela lista atualizada de usuários
def get_users(server):
    global avaiable_users
    response = send_req(server, 'users', [])
    users = [u for u in response['response'] if u[0] != username]
    log.users(users)

#Busca por um usuário no sistema
def get_user(server, name):
    response = send_req(server, 'user', [name])
    user = response['response']
    if user and len(user) == 3:
        if user[0] in avaiable_users and avaiable_users[user[0]]['endr'] != [user[1], user[2]]:
            if avaiable_users[user[0]]['socket']: avaiable_users[user[0]]['socket'].close()
            avaiable_users[user[0]] = { 'endr': [user[1], user[2]], 'socket': None }
        elif user[0] not in avaiable_users:
            avaiable_users[user[0]] = { 'endr': [user[1], user[2]], 'socket': None }
    elif name in avaiable_users:
        avaiable_users.pop(name, None)
    return user
    
#estabele conexão no endereço de escuta do usuario user
def create_connection(endr):
    try:
        sock = socket.socket()
        sock.connect((endr[0], endr[1]))
        sock.setblocking(False)
        inputs.append(sock)
        return sock
    except ConnectionRefusedError:
        return None

def check_for_user(user, server):
    get_user(server, user)
    if user not in avaiable_users:
        return False
    return True

#Envia mensagem msg ao usuario de nome user.
def send_msg(user, msg, server):
    if user not in avaiable_users and not check_for_user(user, server):
        log.cannot_receive_msg()
        return

    if not avaiable_users[user]['socket']:
        while True:
            avaiable_users[user]['socket'] = create_connection(avaiable_users[user]['endr'])
            if not avaiable_users[user]['socket']:
                if not check_for_user(user, server):
                    log.cannot_receive_msg()
                    return
            else: break
        
    msg = username + ' ' + msg
    data = str(len(msg) + BYTES_LEN).zfill(BYTES_LEN) + msg
    try:
        sock = avaiable_users[user]['socket']
        sock.sendall(bytes(data, encoding='utf-8'))
    except ConnectionRefusedError:
        log.cannot_receive_msg()

#Garante o recv completo da mensagem usando os BYTES_LEN primeiros bytes para
#indicar o tamanho da mensagem
def recv_msg(sock):
    chunks = []
    if chunks_rest:
        chunks = chunks_rest.copy()
        chunks_rest.clear()
    recebidos = 0
    msg_len = BYTES_LEN
    while recebidos < msg_len:
        chunk = sock.recv(2048)
        if not chunk: return None
        chunks.append(chunk)
        recebidos = recebidos + len(chunk)
        if recebidos >= BYTES_LEN and msg_len == BYTES_LEN:
            size = str(b''.join(chunks), encoding='utf-8')[0:BYTES_LEN]
            msg_len = int(size)
    if recebidos > msg_len:
        chunks_rest.append(chunks[-1][(msg_len-recebidos):])
        chunks[-1] = chunks[-1][0:(msg_len-recebidos)]
    return str(b''.join(chunks), encoding='utf-8')[BYTES_LEN:]

#Recebe e exibe a mensagem, associando o socket ao usuário, caso ainda não esteja associado.
def show_msg(sock, server):
    response = recv_msg(sock)
    if not response:
        sock.close()
        if sock in inputs:
            inputs.remove(sock)
        user = list(avaiable_users.keys())[[x['socket'] for x in list(avaiable_users.values())].index(sock)]
        if user:
            avaiable_users[user]['socket'] = None
        return 
    user = response.split(' ', 1)[0]
    msg = response.split(' ', 1)[1]
    if user not in avaiable_users:
        get_user(server, user)
    if avaiable_users[user]['socket'] != sock:
        avaiable_users[user]['socket'] = sock

    log.message(user, msg)
            
#Encerra a conexão iniciada com todos os clientes
def close_client_sockets():
    for user in avaiable_users.keys():
        if avaiable_users[user]['socket']:
           avaiable_users[user]['socket'].close() 

def main():
    server = socket.socket() #AF_INET, SOCK_STREAM por default
    server.connect((HOST, PORTA)) #estabelece conexao com o servidor

    mysock = socket.socket()
    mysock.bind((MYHOST, MYDOOR))
    mysock.listen(10)
    mysock.setblocking(False)
    inputs.append(mysock)

    log.start_application()

    login(server)

    while True:
        read, write, conect = select.select(inputs, [], [])
        for req in read:
            if req == sys.stdin:
                cmd = input()
                if cmd == 'exit':
                    server.close()
                    close_client_sockets()
                    sys.exit()

                if cmd.startswith('/msg'):
                    words = cmd.strip().split()
                    user = words[1]
                    if is_valid_username(user): 
                        msg = ' '.join(words[2:])
                        send_msg(user, msg, server)
                    else:
                        print('Nome de usuário inválido. O nome de usuário deve conter apenas letras e números')
                elif cmd.startswith('/users'):
                    get_users(server)
                elif cmd.startswith('/user'):
                    words = cmd.strip().split()
                    user = words[1]
                    user = get_user(server, user)
                    log.user_data(user)
            elif req == mysock:
                newSock, endr = mysock.accept()
                inputs.append(newSock)
                
            else: #is a user socket
                show_msg(req, server)


main()
