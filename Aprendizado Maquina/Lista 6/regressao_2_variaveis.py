# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:33:52 2019

@author: joyce
"""


from mpl_toolkits import mplot3d


from numpy import matmul
from numpy import array
from numpy.linalg import inv
import numpy as np
import csv
import matplotlib.pyplot as plt


def getDados():
    with open('train_data.csv') as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                x.append([float(row[1]), float(row[2]), float(row[3])])
            line_count += 1
    return x

def getTeste():
    with open('test_data.csv') as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                x.append([float(row[1]), float(row[2]), float(row[3])])
            line_count += 1
    return x

def montaMatriz(dados, d):
    x = []
    z = []
    xdados = []
    ydados = []
    for dado in dados:
        linha = []
        for i in range(0, d+1):
            if i == 0:
                linha.append(1)
            else:
                linha.append(pow(dado[0], i))
        for i in range(0, d):
            linha.append(pow(dado[1], i+1))
        xdados.append(dado[0])
        ydados.append(dado[1])
        x.append(linha)
        z.append(dado[2])
    return x, z, xdados, ydados

def regressao (d):
    x, z, xdados, ydados = montaMatriz(getDados(), d)
    x = array(x)
    z = array(z)
    w = matmul( matmul(inv(matmul(x.transpose(), x)), x.transpose()), z )
    
    xtest, ztest, xdados_test, ydados_test = montaMatriz(getTeste(),d)
    
    temp = ztest - matmul(xtest,w)
    nll = 1/2 * matmul(temp.transpose(), temp)
    return xdados_test, ydados_test, ztest, w, xtest, nll

def plotFunc(d):
    xdados, ydados, zdados, w, x, nll = regressao(d)
    y = matmul(x,w)
    # Data for a three-dimensional line
    ax = plt.axes(projection='3d')
    ax.scatter3D(xdados, ydados, y, 'gray')
    return nll

def plotData(d):
    xdados, ydados, zdados, w, x, nll = regressao(d)
    
    ax2 = plt.axes(projection='3d')
    # Data for three-dimensional scattered points
    ax2.scatter3D(xdados, ydados, zdados, cmap='Greens');
    return nll