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
                x.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
            line_count += 1
    return x

def getTeste():
    with open('test_data.csv') as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                x.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
            line_count += 1
    return x

def montaMatriz(dados, d):
    x = []
    z = []
    for dado in dados:
        linha = []
        for i in range(0, d+1):
            if i == 0:
                linha.append(1)
            else:
                linha.append(pow(dado[0], i))
        for i in range(0, d):
            linha.append(pow(dado[1], i+1))
        
        for i in range(0, d):
            linha.append(pow(dado[2], i+1))
        x.append(linha)
        z.append(dado[3])
    return x, z

def regressao (d):
    x, z = montaMatriz(getDados(), d)
    xtest, ztest = montaMatriz(getTeste(), d)
    x = array(x)
    z = array(z)
    w = matmul( matmul(inv(matmul(x.transpose(), x)), x.transpose()), z )
    temp = ztest - matmul(xtest,w)
    nll = 1/2 * matmul(temp.transpose(), temp)
    return nll







