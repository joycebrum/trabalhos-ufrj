from numpy import matmul
from numpy import array
from numpy.linalg import inv

x1 = [ 334, 438, 520, 605, 672, 767 ]
y1 = [ [39300], [60000], [68500], [86000], [113000], [133000] ]

entrada1 = [848, 912]

def regressao(X, y):
    return matmul(matmul(inv(matmul(X.transpose(), X)),X.transpose()), y)

def Q1_modelo1(d, y):
    X = []
    for v in d:
        X.append([1, v])
    X = array(X)
    return regressao(X, y)

def Q1_modelo2(d, y):
    X = []
    for v in d:
        X.append([1, v, pow(v,2), pow(v,3), pow(v,4)])
    X = array(X)
    return regressao(X, y)

def Q1_modelo1_erro():
    X = []
    for v in d:
        X.append([1, v])
    X = array(X)
    
    w = regressao(X, y1)
    somatorio = 0
    for v in x1:
        m = array([1, v])
        v = matmul(m, w)
        somatorio = pow(v - )
    

    
        
