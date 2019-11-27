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
                if float(row[0]) < 40 :
                    if c != 0:
                        continue
                elif float(row[0]) < 60:
                    if c != 1:
                        continue
                else:
                    if c != 2:
                        continue
                x.append([float(row[1]), float(row[2]), float(row[3])])
            line_count += 1
    return x
def getDados(c):
    return getGenerico('train_data.csv',c)

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
def v0Max(indice1, indice2, c):
    u, s, n= mi_sigma(getDados(c))
    dados = getTestes(c)
    somaErro = 0
    for i in range (0, len(dados)):
        x = calcV(i, u, s, dados)
        somaErro += abs(x - dados[i][2])/dados[i][2]
    somaErro /= len(dados)  
    print('erro médio: ', somaErro)
    return somaErro

v0Max(78,100, 0)
print('\n')
v0Max(78,201, 1)
print('\n')
v0Max(78,201, 2)