#Cliente - camada de interface com o cliente

import socket
import json
import ast

HOST = 'localhost' 
PORTA = 5000

#criar o descritor de socket
sock = socket.socket() #AF_INET, SOCK_STREAM por default

#estabelecer conexao
sock.connect((HOST, PORTA))

print("Para encerrar digite 'exit'")
print("Digite o nome do arquivo que deseja processar")

while True:
    user_input = input()
    if user_input == 'exit': break

    #enviar nome do arquivo
    sock.send(bytes(user_input, encoding='utf-8'))

    data = sock.recv(1024)

    try: #tenta imprimir palavras da lista
        lista = eval(data.decode())

        for element in lista:
            print(element[0], "-", element[1])
    except: #caso nao consiga, imprimir a string retornada (caso de erro)
        print(data.decode())
    print('')
#encerrar a conexao
sock.close()
