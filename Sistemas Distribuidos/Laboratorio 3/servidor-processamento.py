#Servidor - camada de processamento de dados

import socket
import json
import ast
import re

HOST = 'localhost' 
PORTA = 5000 #porta da camada atual de processamento de dados
DBPORTA = 5010 #porta da camada de acesso aos dados do servidor

def get_10_word_more_frequent(text): #contabiliza, ordena e retorna as 10 palavras mais frequentes
    counts = {}
    words = re.sub(' +', ' ', text.replace('\n', ' ').replace('\t', ' ').replace('/', ' ').replace('(', '').replace(')', '')).strip().lower().split(' ')
    for word in words:
        if word not in counts:
            counts[word] = words.count(word)
    sorted_words = [k for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)]

    if len(sorted_words)>10:
        sorted_words = sorted_words[:10]

    pairs = []

    for word in sorted_words:
        pairs.append((word, counts[word]))
    return pairs
    
#criar descritor socket de escuta
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet e TCP
#vincula o endereco e porta
sock.bind((HOST, PORTA))

#criar descritor socket de conexao
dbSock = socket.socket()
#conectar com a camada de acesso aos dados do servidor
dbSock.connect((HOST, DBPORTA))

#colocar-se em modo de espera
sock.listen(1)

while True:
    #aceitar conexao com um novo cliente
    novoSock, endereco = sock.accept()
    while True:
        #esperar pelo nome do arquivo
        filename = novoSock.recv(1024)
        if not filename: break
        
        dbSock.send(filename) #solicitar dados do arquivo a camada de acesso aos dados

        #receber conteudo do arquivo
        data = dbSock.recv(4294967296)
        
        str_data = str(data, encoding='utf-8')#passar para o formato string
        data_string = ast.literal_eval(str_data)#transformar de string em dictionary
        
        if data_string['status'] == 0: #se for sucesso
            lista = get_10_word_more_frequent(data_string["data"])
            novoSock.send(str(lista).encode())#retorna a lista de palavras
        else: #caso de erro
            novoSock.send(bytes(data_string["data"], encoding='utf-8')) #retorna a mensagem
                        

    #fechar o descritor de socket da conexao com o cliente
    novoSock.close()

#fechar o descritor do socket principal
sock.close()
dbSock.close()                          
