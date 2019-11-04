from numpy import matmul
from numpy import array
from numpy.linalg import inv

x1 = [ 334, 438, 520, 605, 672, 767 ]
y1 = [ [39300], [60000], [68500], [86000], [113000], [133000] ]

entrada1 = [848, 912]

def modelo1():
    global x1
    global y1
    X = []
    for v in x1:
        X.append([1, v])
    X = array(X)
    return matmul(matmul(inv(matmul(X.transpose(), X)),X.transpose()), y1)

def modelo2():
    global x1
    global y1
    X = []
    for v in x1:
        X.append([1, ])
    

    
        
