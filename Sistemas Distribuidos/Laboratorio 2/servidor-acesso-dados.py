#Servidor - camada de acesso aos dados

import socket

HOST = '192.168.0.13'
PORTA = 5010

#criar descritor socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet e TCP

#vincula o endereco e porta
sock.bind((HOST, PORTA))

#colocar-se em modo de espera
sock.listen(1)

while True:
    novoSock, endereco = sock.accept()
    while True:
        filename = novoSock.recv(1024) #recebe o nome do arquivo
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
        novoSock.send(bytes(str(data), encoding='utf-8')) #envia o dict
        print("")

    novoSock.close()

#fechar o descritor do socket principal
sock.close()
