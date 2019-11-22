from numpy import matmul
from numpy import array
from numpy.linalg import inv
import numpy as np
import csv
def getGenerico(arquivo):
    with open(arquivo) as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                x.append([float(row[0]),float(row[1]), float(row[2]), float(row[3])])
            line_count += 1
    return x
def getDados():
    return getGenerico('train_data.csv')

def mi_sigma(dados):
    somatorio = [0,0,0,0]
    sigma = array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]).reshape(4,4)
    N = 0
    dados = array(dados)
    for dado in dados:
        somatorio += dado
        N = N + 1
    u = np.transpose(array(somatorio / N).reshape(1,4))
    for dado in dados:
        norm =  np.transpose(array(dado).reshape(1,4)) - u
        sigma = sigma + matmul(norm, norm.transpose())
    sigma = sigma/ N
    return u, sigma, N
    
def v0Max(indice1, indice2):
    u, s, n= mi_sigma(getDados())
    dados = getDados()
    inversa  = inv(s)
    x1 = u[3]
    som = 0
    for i in range(0,len(s[0])):
        if i != 3:
            som += inversa[3][i] * (dados[indice1][i]-u[i])
    x1 -= som/(2*inversa[3][3])
    print('v0 estimado = ', x1, ' v0 certo', dados[indice1][3])
    x2 = u[3]
    som = 0
    for i in range(0,len(s[0])):
        if i != 3:
            som += inversa[3][i] * (dados[indice2][i]-u[i])
    x2 -= som/(2*inversa[3][3])
    print('v0 estimado = ', x2, ' v0 certo', dados[indice2][3])

v0Max(78,201)