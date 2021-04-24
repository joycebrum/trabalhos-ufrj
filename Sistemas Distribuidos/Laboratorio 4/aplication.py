#Cliente - camada de interface com o cliente

import socket
import json
import ast

HOST = 'localhost' 
PORTA = 5010

username = ''

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

def send_req(server, operation, args):
    req = json.dumps({"requisition": { "operation": operation, "arguments": args}})
    server.sendall(bytes(req, encoding='utf-8')) #envia a requisicao

    return recvall(server)
    

def login(server):
    global username
    while True:
        user_input = input()
        if user_input == 'exit': break

        response = send_req(server, 'login', [user_input.strip()])
        
        if response['response'][0] == 0:
            print('Nome de usuário cadastrado com sucesso. Bem vindo(a)', user_input)
            username = user_input.strip()
            break
        else:
            print('Nome de usuário já em uso. Escolha outro.')

def cmd_users(server):
    response = send_req(server, 'users', [])
    print('\n------------------------------------------------------')
    print('                      Usuários                        ')
    users = [u for u in response['response'] if u[0] != username]
    if len(users) == 0:
        print('Não há usuários ativos')
    else:
        for user in users:
            print(user[0], '---', user[1], user[2]) 
    print('------------------------------------------------------\n')

def cmd_user(server, name):
    response = send_req(server, 'user', [name])
    print('\n------------------------------------------------------')
    user = response['response']
    if not user or len(user) == 0:
        print('Não foi possível encontrar este usuário no sistema.')
    else:
        print(user[0], '---', user[1], user[2]) 
    print('------------------------------------------------------\n')
    
def chat_commands(server):
    while True:
        user_input = input()
        if user_input == 'exit': break

        if user_input.startswith('/msg'):
            words = user_input.strip().split()
            user = words[1]
            msg = ' '.join(words[2:])
            print('para', user, 'mensagem', msg)
        elif user_input.startswith('/users'):
            cmd_users(server)
        elif user_input.startswith('/user'):
            words = user_input.strip().split()
            user = words[1]
            cmd_user(server, user)
            

def main():
    server = socket.socket() #AF_INET, SOCK_STREAM por default
    server.connect((HOST, PORTA)) #estabelece conexao com o servidor
    
    print("Para encerrar digite 'exit'")
    print("Bem vindo, digite o seu nome de usuário")

    login(server)

    chat_commands(server)
            
    #encerrar a conexao
    server.close()


main()
