#Servidor - camada de processamento de dados

import socket
import ast
import re
import sys
import select
import multiprocessing

HOST = 'localhost' 
PORTA = 5020 #porta da camada atual de processamento de dados
DBPORTA = 5010 #porta da camada de acesso aos dados do servidor

#entrada padrao como input inicial 
inputs = [sys.stdin]

def get_10_word_more_frequent(text): #contabiliza, ordena e retorna as 10 palavras mais frequentes
    '''Calcula a ocorrencia de todas as palavras da string de entrada e retorna as
    10 palavras mais frequentes
    Entrada: texto a ser analizado no formato string
    Saida: lista de tuplas do tipo (palavra, frequencia)'''
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

def startServer():
    '''Inicia o socket de conexao por onde sera estabelecida a conexao com a
    camada de interface sempre que houver um novo cliente.
    Saida: retorna o socket de conexao'''
    #criar descritor socket de escuta
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Internet e TCP

    #vincula o endereco e porta
    sock.bind((HOST, PORTA))

    #colocar-se em modo de espera
    sock.listen(5)
    sock.setblocking(False)

    inputs.append(sock)
	
    return sock

def connectToDbSock():
    '''Conecta com a camada de acesso aos dados
    Saida: retorna o socket de conexao com a camada de acesso aos dados'''
    dbSock = socket.socket() #criar descritor socket de conexao
	
    dbSock.connect((HOST, DBPORTA)) #conectar com a camada de acesso aos dados do servidor
    return dbSock

def acceptConnection(sock):
    '''Aceita uma nova conexao com a camada de processamento do servidor	
    Entrada: socket da camada de dados(atual) do servidor
    Saída: o novo socket de conexao e o endereco a camada de processamento''' 
    newSock, endr = sock.accept()
    return newSock, endr
    
def answerRequisition(newSock, endr):
    '''Faz todo o tratamento do cliente ate o encerramento da conexao
    Entrada: socket do cliente e endereco'''
    dbSock = connectToDbSock()
    while True:
        filename = newSock.recv(1024) #espera pelo nome do arquivo
        if not filename: break
		
        dbSock.send(filename) #solicitar dados do arquivo a camada de acesso aos dados

        data = dbSock.recv(4294967296) #receber conteudo do arquivo
		
        str_data = str(data, encoding='utf-8')
        data_string = ast.literal_eval(str_data)#transformar de string em dictionary
		
        if data_string['status'] == 0: #se for sucesso
            lista = get_10_word_more_frequent(data_string["data"])
            newSock.send(str(lista).encode())#retorna a lista de palavras
        else: #caso de erro
            newSock.send(bytes(data_string["data"], encoding='utf-8')) #retorna a mensagem de arquivo nao encontrado
    dbSock.close()
    newSock.close()
    
def main():
    sock = startServer()
    print("Camada de processamento do servidor iniciada. Para encerra-la digite exit")
    clients = []
    history = []
    while True:
        read, write, conect = select.select(inputs, [], [])
        for req in read:
            if req == sock:
                newSock, endr = acceptConnection(sock)
                history.append(endr)
                print ('Conectado com: ', endr)
                #cria um fluxo dedicado ao cliente
                client = multiprocessing.Process(target=answerRequisition, args=(newSock, endr))
                client.start()
                clients.append(client)
            elif req == sys.stdin:
                cmd = input()
                if cmd == 'exit':
                    print("Aguardando clientes terminarem para encerrar")
                    for c in clients:
                        c.join()
                    print("Encerrando...")
                    sock.close()
                    sys.exit()
                if cmd == 'hist': #prints all served clients
                    print("-------------------------------------")
                    if len(history) == 0:
                        print("Não houve conexão com nenhum cliente")
                    else:
                        for c in history:
                            print(c)
                    print("-------------------------------------")
main()                       
