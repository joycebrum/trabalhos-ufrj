import math
import csv
def getGenerico(nomeArq):
    with open(nomeArq) as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                c = 2
                if float(row[0]) < 40: 
                    c = 0
                elif float(row[0]) < 60:
                    c = 1
                x.append([c,float(row[1]),float(row[2]), float(row[3])])
            line_count += 1
    return x
def getDados():
    return getGenerico('train_2_data.csv')
def getTeste():
    return getGenerico('test_2_data.csv')

def train(dados):
    Nc = [0,0,0]
    ucj = [[0,0,0],
           [0,0,0],
           [0,0,0]]
    s2cj = [[0,0,0],
           [0,0,0],
           [0,0,0]]
    N = 0
    for dado in dados:
        Nc[dado[0]] += 1
        ucj[dado[0]][0] += dado[1]
        ucj[dado[0]][1] += dado[2]
        ucj[dado[0]][2] += dado[3]
        N = N + 1
    for i in range(0,3):
        for j in range(0,3):
            if Nc[i] > 0:
                ucj[i][j] /= Nc[i]
    for dado in dados: 
        s2cj[dado[0]][0] += pow( dado[1] - ucj[dado[0]][0], 2 )
        s2cj[dado[0]][1] += pow( dado[2] - ucj[dado[0]][1], 2 )
        s2cj[dado[0]][2] += pow( dado[3] - ucj[dado[0]][2], 2 )
    for i in range(0,3):
        for j in range(0,3):
            if Nc[i] > 0:
                s2cj[i][j] /= Nc[i]
            
    return N, Nc, ucj, s2cj

def predict():
    dados = getDados()
    testes = getTeste()
    N, Nc, ucj, s2cj = train(dados)
    acertos = 0
    erros = 0
    total = 0
    for teste in testes:
        total += 1
        id1 = prob(0,teste,N, Nc, ucj, s2cj)
        id2 = prob(1,teste,N, Nc, ucj, s2cj)
        id3 = prob(2,teste,N, Nc, ucj, s2cj)
        if teste[0] == id1:
            if id1 > id2 and id1 > id3:
                acertos += 1
            else:
                erros += 1
        elif teste[0] == id2:
            if id2 > id1 and id2 > id3:
                acertos += 1
            else:
                erros += 1
        else:
            if id3 > id1 and id3 > id2:
                acertos += 1
            else:
                erros += 1
    return acertos/total, erros/total, total

def prob(classe, dado, N, Nc, ucj, s2cj):
    pi_c = Nc[classe] / N
    prob = 1
    for i in range(1, len(dado)):
        prob *= Normal(ucj[classe][i-1], s2cj[classe][i-1], dado[i])
    return pi_c * prob

def Normal(u, s2, x) :
    expoente = -pow(x-u,2) / (2*s2)
    return math.exp(expoente) / (math.sqrt(2*math.pi*s2))

predict()