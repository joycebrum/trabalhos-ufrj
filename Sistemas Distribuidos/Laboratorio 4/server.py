#Servidor - camada de processamento de dados

import socket
import sys
import select
import json
import threading

HOST = 'localhost' 
PORTA = 5010 #porta da camada atual de processamento de dados

#entrada padrao como input inicial 
inputs = [sys.stdin]
clients = {}
threads = []
lock = threading.Lock()

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
            

def startServer():
    '''Inicia o socket de conexao por onde sera estabelecida a conexao com a
    camada de interface sempre que houver um novo cliente.
    Saida: retorna o socket de conexao'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet e TCP
    sock.bind((HOST, PORTA))

    sock.listen(10)
    sock.setblocking(False)

    inputs.append(sock)
	
    return sock

def acceptConnection(sock):
    '''Aceita uma nova conexao com a camada de processamento do servidor	
    Entrada: socket da camada de dados(atual) do servidor
    Saída: o novo socket de conexao e o endereco a camada de processamento''' 
    newSock, endr = sock.accept()
    return newSock, endr

def login(username, endr):
    response = 1
    lock.acquire()
    if username not in clients:
        clients[username] = endr
        response = 0
        print('Usuário', username, 'conectado no endereço', endr)
    lock.release()
    return {'response': [response]}

def logout(endr):
    lock.acquire()
    username = list(clients.keys())[list(clients.values()).index(endr)]
    clients.pop(username, None)
    lock.release()
    print('Usuário', username, 'desconectado do endereço', endr)

def get_users():
    lock.acquire()
    curr_users = [[key, clients[key][0], clients[key][1]] for key in clients]
    lock.release()
    return { 'response': curr_users }

def get_user(username):
    user = None
    lock.acquire()
    if username in clients: user = clients[username]
    lock.release()
    if not user: return {'response': [] }
    return {'response': [username, user[0], user[1]] }
    
def answerRequisition(newSock, endr):
    '''Analiza a requisição para definir qual a operação que deve ser realizada
    Entrada: socket do cliente e endereco'''
    while True:
        requisition = recvall(newSock)
        if not requisition: break

        oper = requisition['requisition']['operation']
        if oper == 'login':
            answer = login(requisition['requisition']['arguments'][0], endr)
        elif oper == 'users':
            answer = get_users()
        elif oper == 'user':
            answer = get_user(requisition['requisition']['arguments'][0])
        
        newSock.send(bytes(json.dumps(answer), encoding='utf-8')) #retorna o response
    logout(endr)
    newSock.close()
        
def main():
    sock = startServer()

    while True:
        read, write, conect = select.select(inputs, [], [])
        for req in read:
            if req == sock:
                newSock, endr = acceptConnection(sock)
                #cria um fluxo dedicado ao cliente
                thread = threading.Thread(target=answerRequisition, args=(newSock, endr))
                thread.start()
                threads.append(thread)
                
            elif req == sys.stdin:
                cmd = input()
                if cmd == 'exit':
                    print("Aguardando clientes terminarem para encerrar")
                    for c in threads:
                        c.join()
                    print("Encerrando...")
                    sock.close()
                    sys.exit()
main()                       
    
