#Servidor - camada de acesso aos dados

import socket
import select
import sys

#localizacao do servidor
HOST = 'localhost'
PORTA = 5010

#entrada padrao como input inicial 
inputs = [sys.stdin]

def startServer():
    #criar descritor socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet e TCP

    #vincula o endereco e porta
    sock.bind((HOST, PORTA))

    #colocar-se em modo de espera
    sock.listen(1)
    
    inputs.append(sock)
    return sock

def acceptConnection(sock):
    '''Aceita uma nova conexao com a camada de processamento do servidor
    Entrada: socket da camada de dados(atual) do servidor
    Saída: o novo socket de conexao e o endereco a camada de processamento'''    
    newSock, endereco = sock.accept()
    return newSock, endereco

def answerRequisition(cliSock, endr):
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
    print("Servidor iniciado. Para encerra-lo digite exit")
    while True:
        read, write, conect = select.select(inputs, [], [])
        for req in read:
            if req == sock:
                newSock, endr = acceptConnection(sock)
                answerRequisition(newSock, endr)
            elif req == sys.stdin:
                cmd = input()
                if cmd == 'exit':
                    sock.close()
                    sys.exit()


main()

