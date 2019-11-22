from numpy import matmul
from numpy import array
from numpy.linalg import inv
import csv
import matplotlib.pyplot as plt


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

def getTeste():
    with open('test_data.csv') as csv_file:
        x = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                x.append([float(row[2]), float(row[3])])
            line_count += 1
    return x

def montaMatriz(dados, d):
    x = []
    y = []
    xdados = []
    for dado in dados:
        linha = []
        for i in range(0, d+1):
            if i == 0:
                linha.append(1)
            else:
                linha.append(pow(dado[0], i))
        xdados.append(dado[0])
        x.append(linha)
        y.append(dado[1])
    return x,y,xdados

def regressao (d):
    dados = getDados()
    x,y, xdados = montaMatriz(dados, d)
    x = array(x)
    y = array(y)
    w = matmul( matmul(inv(matmul(x.transpose(), x)), x.transpose()), y )
    xtest, ytest, xdadostest = montaMatriz(getTeste(), d)
    plotData(xdadostest, ytest)
    plotFunction(w, xtest, xdadostest)
    temp = ytest - matmul(xtest,w)
    nll = 1/2 * matmul(temp.transpose(), temp)
    return nll

def plotData(xdados, y):
    plt.plot(xdados, y, 'ro')
    plt.axis([0, 450, 0, 100])
    plt.show()
    
def plotFunction(w, x, xdados):
    y = matmul(x, w)
    plt.plot(xdados, y)
    plt.axis([0, 450, 0, 100])
    
regressao(1)
#regressao(2)