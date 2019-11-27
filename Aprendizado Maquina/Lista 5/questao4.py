import csv
from math import exp
def EM():
    gama = 0
    mi=[1,1]
    pi=[0.5,0.5]
    x =[]
    with open('quatro.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        column_area = 0
        column_value = 0
        for row in csv_reader:
            x.append(float(row[0].strip()))
            line_count += 1
    for i in range (0,3):
        novomi = 0
        for v in x:
            gama = pi[0]*exp(-pow(x[i]-mi[0],2))/(pi[0]*exp(-pow(x[i]-mi[0],2)) + pi[1]*exp(-pow(x[i]-mi[1],2)))
            novomi = gama * (x[i]-mi[0])
        mi[0] = novomi
    return mi
