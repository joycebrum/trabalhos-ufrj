import csv
from numpy import matmul
from numpy import array
from numpy.linalg import inv
from math import log
from math import sqrt
from math import exp
next_x = array([1,1])  # We start the search at x=6
gamma = 0.01  # Step size multiplier
precision = 0.00001  # Desired precision of result
max_iters = 10000  # Maximum number of iterations

fator_normalizacao = 10000
def norma(x) :
  norma = 0
  for v in x:
    norma = norma + pow(v,2)
  return sqrt(norma)

# Derivative function
def df(w, x, y):
    dx = [0,0]
    for i in range(0, len(x)):
        dx[0] += y[i] - exp(w[0]+w[1]*x[i])/(1+exp(w[0]+w[1]*x[i]))
        dx[1] += y[i]*x[i] - exp(w[0]+w[1]*x[i])*(x[i]/(1+exp(w[0]+w[1]*x[i])))
    return array(dx)
def minimum():
    global next_x
    global gamma
    global max_iters
    global precision
    x,y = getCsv()
    for _i in range(max_iters):
        current_x = next_x
        d = df(current_x,x,y)
        next_x = current_x - gamma * d
        step = next_x - current_x
        print(_i, current_x)
        if norma(step) <= precision:
            break
    return current_x


# The output for the above will be something like
# "Minimum at 2.2499646074278457"

def getCsv():
    x = []
    y = []
    with open('train.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        column_area = 0
        column_value = 0
        for row in csv_reader:
            if line_count == 0:
                for column in row :
                    if column == 'LotArea':
                        break
                    column_area = column_area + 1
                for column in row :
                    if column == 'SalePrice':
                        break
                    column_value = column_value + 1
                line_count += 1
            else:
                x.append(int(row[column_area])/fator_normalizacao)
                y.append(int(row[column_value])/fator_normalizacao)        
                line_count += 1
        N = line_count - 1
    return x,y
