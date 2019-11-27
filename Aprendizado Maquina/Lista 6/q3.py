# -*- coding: utf-8 -*-
from numpy import matmul
from numpy import array
from numpy.linalg import inv
import csv
import matplotlib.pyplot as plt
"""
Created on Sat Nov 16 00:17:35 2019

@author: joyce
"""
def getDados():
    with open('train_data.csv') as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                x.append([float(row[2]), float(row[3])])
            line_count += 1
    return x

def mi_sigma(dados):
    somatorio = [0,0]
    sigma = array([0,0])
    N = 0
    dados = array(dados)
    for dado in dados:
        somatorio += dado
        N = N + 1
    u = somatorio / N
    for dado in dados:
        norm =  dado - u
        vec = array(norm)
        sigma = sigma + matmul(vec, vec.transpose())
    sigma = sigma/ N
    return u, sigma

def calc()    
    u, s= mi_sigma(getDados())
