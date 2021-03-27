#lado ativo

import socket

HOST = '192.168.0.13' 
PORTA = 5000

#criar o descritor de socket
sock = socket.socket() #AF_INET, SOCK_STREAM por default

#estabelecer conexao
sock.connect((HOST, PORTA))

print("Para encerrar digite 'exit'")

while True:
    user_input = input()
    if user_input == 'exit': break

    #enviar mensagem de digitada
    sock.send(bytes(user_input, encoding='utf-8'))

    #receber resposta do lado passivo
    msg = sock.recv(1024)
    print(str(msg, encoding='utf-8'))

#encerrar a conexao
sock.close()
