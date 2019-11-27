from numpy import matmul
from numpy import array
from numpy.linalg import inv

x1 = [ 334, 438, 520, 605, 672, 767 ]
y1 = [ [39300], [60000], [68500], [86000], [113000], [133000] ]

entrada1 = [848, 912]
def montaMatriz(modelo):
    X = []  
    if modelo == 1:
        for v in x1:
            X.append([1, v])
        X = array(X)
    else :
        for v in x1:
            X.append([1, v, pow(v,2), pow(v,3), pow(v,4)])
        X = array(X)
    return X
def regressao(X, y):
    return matmul(matmul(inv(matmul(X.transpose(), X)),X.transpose()), y)

def Q1_modelo1():
    X = montaMatriz(1)
    return regressao(X, y1)

def Q1_modelo2():
    X = montaMatriz(2)
    return regressao(X, y1)

def Q1_modelo1_erro():
    w = Q1_modelo1()
    somatorio = 0
    i = 0
    for v in x1:
        m = array([1, v])
        res = matmul(m, w)
        somatorio = somatorio + pow(res[0] - y1[i][0],2)
        i = i + 1
    return somatorio/i
def Q1_modelo2_erro():
    w = Q1_modelo2()
    somatorio = 0
    i = 0
    for v in x1:
        m = array([1, v, pow(v,2), pow(v,3), pow(v,4)])
        res = matmul(m, w)
        somatorio = somatorio + pow(res[0] - y1[i][0],2)
        i = i + 1
    return somatorio/i

def valorEstimado(modelo, v):
    if modelo == 1:
        w = Q1_modelo1()
        x = array([1, v])
        return matmul(x, w)
    else :
        w = Q1_modelo2()
        x = array([1, v, pow(v,2), pow(v,3), pow(v,4)])
        return matmul(x,w)

def erroQuadratico(modelo):
    estimado = valorEstimado(modelo, 848)
    somatorio = pow(estimado - 155900,2)
    estimado = valorEstimado(modelo, 912)
    somatorio = somatorio + pow(estimado - 156000,2)
    return somatorio[0] /2
    
    
        
