from numpy import matmul
from numpy import array
from numpy.linalg import inv
import numpy as np
import csv
import math 
import matplotlib.pyplot as plt
def getGenerico(arquivo):
    with open(arquivo) as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                x.append([float(row[2]), float(row[3])])
            line_count += 1
    return x
def getDados():
    return getGenerico('train_data.csv')
def getTeste():
    return getGenerico('test_data.csv')

def mi_sigma(dados):
    somatorio = [0,0]
    sigma = array([[0,0],[0,0]]).reshape(2,2)
    N = 0
    dados = array(dados)
    for dado in dados:
        somatorio += dado
        N = N + 1
    u = np.transpose(array(somatorio / N).reshape(1,2))
    for dado in dados:
        norm =  np.transpose(array(dado).reshape(1,2)) - u
        sigma = sigma + matmul(norm, norm.transpose())
    sigma = sigma/ N
    return u, sigma, N


def Normal(u, s, x) :
    expoente = -pow(x-u,2) / (2*s)
    return math.exp(expoente) / (math.sqrt(2*math.pi * np.linalg.det(s)))
    

def calc():
    u, s, n= mi_sigma(getDados())
    
    # 100 linearly spaced numbers
    x = np.linspace(-100,100,100)
    
    # the function, which is y = x^2 here
    y = Normal(u[0])
    
    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    # plot the function
    plt.plot(x,y, 'r')
    
    # show the plot
    plt.show()
    
calc()