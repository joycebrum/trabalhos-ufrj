#Servidor - camada de acesso aos dados

import socket
import select
import sys
import multiprocessing
import os

#localizacao do servidor
HOST = 'localhost'
PORTA = 5010

#entrada padrao como input inicial 
inputs = [sys.stdin]

def startServer():
    '''Inicia o socket de conexao por onde sera estabelecida a conexao com a
    camada de processamento sempre que houver um novo cliente.
    Saida: retorna o socket de conexao'''
    #criar descritor socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet e TCP

    #vincula o endereco e porta
    sock.bind((HOST, PORTA))

    #colocar-se em modo de espera
    sock.listen(5)
    sock.setblocking(False)
    
    inputs.append(sock)
    return sock

def acceptConnection(sock):
    '''Aceita uma nova conexao com a camada de processamento do servidor
    Entrada: socket da camada de dados(atual) do servidor
    Saída: o novo socket de conexao e o endereco a camada de processamento'''    
    newSock, endereco = sock.accept()
    return newSock, endereco

def answerRequisition(cliSock, endr):
    '''Faz todo o tratamento do cliente ate o encerramento da conexao
    Entrada: socket do cliente e endereco''' 
    while True:
        filename = cliSock.recv(1024) #recebe o nome do arquivo
        if not filename: break

        data = {"status": 0, "data": "" } #status 0 - sucesso por default
        try:
            print("Procurando o arquivo", str(filename, encoding='utf-8') + ".") 
            my_file_handle = open("db/" + str(filename, encoding='utf-8'), 'r', encoding="utf8")
            data["data"] = my_file_handle.read() 
            print("Arquivo encontrado.")
        except IOError:
            data["status"] = 1 #status de erro
            data["data"] = "Arquivo não encontrado."
            print("Arquivo não encontrado.")
        cliSock.send(bytes(str(data), encoding='utf-8')) #envia o dict
        print("")

    cliSock.close()

def main():
    sock = startServer()
    print("Camada de acesso aos dados do servidor iniciada. Para encerra-la digite exit")
    clients = []
    while True:
        read, write, conect = select.select(inputs, [], [])
        for req in read:
            if req == sock:
                newSock, endr = acceptConnection(sock)
                #cria um fluxo dedicado ao cliente
                client = multiprocessing.Process(target=answerRequisition, args=(newSock, endr))
                client.start()
                clients.append(client)		
            elif req == sys.stdin:
                cmd = input()
                if cmd == 'exit': #encerra a aplicacao
                    print("Aguardando clientes terminarem para encerrar")
                    for c in clients:
                        c.join()
                    print("Encerrando...")
                    sock.close()
                    sys.exit()
                if cmd == 'dir': #lista todos os arquivos do banco
                    print("-------------------------------------")
                    for f in os.listdir("db/"):
                        print(f)
                    print("-------------------------------------")


main()

