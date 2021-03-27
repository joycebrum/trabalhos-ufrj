#lado ativo

import socket

HOST = '192.168.0.13' #se fosse outra maquina aqui seria o IP
PORTA = 5000

#criar o descritor de socket
sock = socket.socket() #AF_INET, SOCK_STREAM por default

#estabelecer conexao
sock.connect((HOST, PORTA))

#enviar mensagem de hello
sock.send(b'Ola, sou o lado ativo!')

#receber resposta do lado passivo
msg = sock.recv(1024)
print(str(msg, encoding='utf-8'))

#encerrar a conexao
sock.close()
