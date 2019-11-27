from numpy import matmul
from numpy import array
from numpy.linalg import inv
import numpy as np
import csv
def getGenerico(arquivo,c):
    with open(arquivo) as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                if c!= -1:
                    if float(row[0]) < 40 :
                        if c != 0:
                            continue
                    elif float(row[0]) < 60:
                        if c != 1:
                            continue
                    else:
                        if c != 2:
                            continue
                else: 
                    x.append([float(row[1]), float(row[2]), float(row[3]), float(row[0])])
                    continue
                x.append([float(row[1]), float(row[2]), float(row[3])])
            line_count += 1
    return x
def getDados(c):
    return getGenerico('train_data.csv',c)
def getTestes(c):
    return getGenerico('test_data.csv',c)

def mi_sigma(dados):
    somatorio = [0,0,0]
    sigma = array([[0,0,0],[0,0,0],[0,0,0]]).reshape(3,3)
    N = 0
    dados = array(dados)
    for dado in dados:
        somatorio += dado
        N = N + 1
    u = np.transpose(array(somatorio / N).reshape(1,3))
    for dado in dados:
        norm =  np.transpose(array(dado).reshape(1,3)) - u
        sigma = sigma + matmul(norm, norm.transpose())
    sigma = sigma/ N
    return u, sigma, N
def calcV(indice, u, s, dados):
    x1 = u[2]
    som = 0
    inversa  = inv(s)
    for i in range(0,len(s[0])):
        if i != 2:
            som += inversa[2][i] * (dados[indice][i]-u[i])
    x1 -= som/(2*inversa[2][2])
    return x1
def v0Max( ):
    for c in range (0, 3):
        somaErro = 0
        u, s, n= mi_sigma(getDados(c))
        testes = getTestes(c)
        for i in range (0, len(testes)):
            x = calcV(i, u, s, testes)
            somaErro += abs(x - testes[i][2])/testes[i][2]
        somaErro /= len(testes)
        print('erro médio classe ', c, ': ', somaErro)

def v0MaxEx10( ):
    somaErro = 0
    u, s, n= mi_sigma(getDados(0))
    u1, s1, n1= mi_sigma(getDados(1))
    u2, s2, n2= mi_sigma(getDados(2))
    testes = getTestes(-1)
    
    for i in range (0, 10):
        if testes[i][3] < 40:
            x = calcV(i, u, s, testes)
        elif testes[i][3]< 60:
            x = calcV(i, u1, s1, testes)
        else:
            x = calcV(i, u2, s2, testes)
        print('valor gerado: ', x, ' valor exato: ', testes[i][2])

v0Max()
v0MaxEx10()