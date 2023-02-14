# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:54:19 2019

@author: joyce
"""

import matplotlib.pyplot as plt
from variables import ALTA
from variables import BAIXA

Clientes_X = [0]
Clientes_X_Max = 0
Clientes_Y = [0]
Clientes_Y_Max = 0

Clientes_X_Classe = {0: [0], 1: [0]}
Clientes_X_Classe_Max = {0: 0, 1: 0}
Clientes_Y_Classe = {0: [0], 1: [0]}
Clientes_Y_Classe_Max = {0: 0, 1: 0}

Espera_X = [0]
Espera_X_Max = 0
Espera_Y = [0]
Espera_Y_Max = 0

Espera_X_Classe = {0: [0], 1: [0]}
Espera_X_Classe_Max = {0: 0, 1: 0}
Espera_Y_Classe = {0: [0], 1: [0]}
Espera_Y_Classe_Max = {0: 0, 1: 0}

Trabalho_Residual_X = [0]
Trabalho_Residual_X_Max = 0
Trabalho_Residual_Y = [0]
Trabalho_Residual_Y_Max = 0

Trabalho_Residual_X_Classe = {0: [0], 1: [0]}
Trabalho_Residual_X_Classe_Max = {0: 0, 1: 0}
Trabalho_Residual_Y_Classe = {0: [0], 1: [0]}
Trabalho_Residual_Y_Classe_Max = {0: 0, 1: 0}

def getTotalPessoasNoSistema(fila1, fila2, servidor):
    if servidor != None:
        return len(fila1) + len(fila2) +1
    else:
        return 0

def getTotalPessoasNoSistemaPorClasse(fila, servidor, priority):
    if servidor != None:
        if servidor.priority == priority:
            return len(fila) + 1
        return len(fila)
    else:
        return 0
def updateGrafoEsperaFilaUnica(fila, time):
    global Espera_X, Espera_Y, Espera_X_Max, Espera_Y_Max
    clientesNaFila = len(fila)
    Espera_X.append(time)
    Espera_X_Max = time
    Espera_Y.append(clientesNaFila)
    if clientesNaFila > Clientes_Y_Max:
        Espera_Y_Max = clientesNaFila
    nq1, nq2 = getQuantFilaPorClasse(fila)
    updateEsperaFilaUnicaComClasse(nq1, ALTA, time)
    updateEsperaFilaUnicaComClasse(nq2, BAIXA, time)

def getQuantFilaPorClasse(fila):
    nq1 = 0
    nq2 = 0
    for cliente in fila:
        if cliente.priority == ALTA:
            nq1 += 1
        else:
            nq2 += 1
    return nq1, nq2

def updateEsperaFilaUnicaComClasse(nq, priority, time):
    global Espera_X_Classe, Espera_Y_Classe 
    global Espera_X_Classe_Max, Espera_Y_Classe_Max
    Espera_X_Classe[priority].append(time)
    Espera_X_Classe_Max[priority] = time
    Espera_Y_Classe[priority].append(nq)
    if nq > Espera_Y_Classe_Max[priority]:
        Espera_Y_Classe_Max[priority] = nq

def updateGrafoTrabalhoResidual(servidor,time):
    global Trabalho_Residual_X, Trabalho_Residual_Y
    global Trabalho_Residual_X_Max, Trabalho_Residual_Y_Max
    Trabalho_Residual_X.append(time)
    Trabalho_Residual_X_Max = time
    if servidor != None:
        Trabalho_Residual_Y.append(servidor.clientData.getTimeRemaining())
        if servidor.clientData.getTimeRemaining() > Trabalho_Residual_Y_Max:
            Trabalho_Residual_Y_Max = servidor.clientData.getTimeRemaining()
    else:
        Trabalho_Residual_Y.append(0)

def updateGrafosFilaUnica(fila, servidor, time):
    global Clientes_X, Clientes_Y, Clientes_X_Max, Clientes_Y_Max
    Clientes_X.append(time)
    Clientes_X_Max = time
    if servidor != None:
        numeroPessoas = len(fila)
    else:
        numeroPessoas = len(fila)+ 1
    Clientes_Y.append(numeroPessoas)
    if numeroPessoas > Clientes_Y_Max:
        Clientes_Y_Max = numeroPessoas
    updateGrafoEsperaFilaUnica(fila, time)
    updateGrafoTrabalhoResidual(servidor,time)
    
def updateGrafos(filaNP, filaP, servidor, time):
    global Clientes_X, Clientes_Y, Clientes_X_Max, Clientes_Y_Max
    clientesNoSistema = getTotalPessoasNoSistema(filaNP, filaP, servidor)
    Clientes_X.append(time)
    Clientes_X_Max = time
    Clientes_Y.append(clientesNoSistema)
    if clientesNoSistema > Clientes_Y_Max:
        Clientes_Y_Max = clientesNoSistema
    updateGrafoClientesClasse(filaP,servidor,time, 0)
    updateGrafoClientesClasse(filaNP,servidor,time, 1)
    
    updateGrafoEspera(filaNP, filaP, time)
    updateGrafoTrabalhoResidual(servidor, time)
    
def updateGrafoClientesClasse(fila, servidor, time, priority):
    global Clientes_X_Classe, Clientes_Y_Classe 
    global Clientes_X_Classe_Max, Clientes_Y_Classe_Max
    clientesNoSistema = getTotalPessoasNoSistemaPorClasse(fila, servidor, priority)
    Clientes_X_Classe[priority].append(time)
    Clientes_X_Classe_Max[priority] = time
    Clientes_Y_Classe[priority].append(clientesNoSistema)
    if clientesNoSistema > Clientes_Y_Classe_Max[priority]:
        Clientes_Y_Classe_Max[priority] = clientesNoSistema
        
def updateGrafoEspera(filaNP, filaP, time):
    global Espera_X, Espera_Y, Espera_X_Max, Espera_Y_Max
    clientesNaFila = len(filaNP) + len(filaP)
    Espera_X.append(time)
    Espera_X_Max = time
    Espera_Y.append(clientesNaFila)
    if clientesNaFila > Clientes_Y_Max:
        Espera_Y_Max = clientesNaFila
    updateGrafoEsperaClasse(filaP,time, 0)
    updateGrafoEsperaClasse(filaNP,time, 1)
    
def updateGrafoEsperaClasse(fila, time, priority):
    global Espera_X_Classe, Espera_Y_Classe 
    global Espera_X_Classe_Max, Espera_Y_Classe_Max
    clientesNaFila = len(fila)
    Espera_X_Classe[priority].append(time)
    Espera_X_Classe_Max[priority] = time
    Espera_Y_Classe[priority].append(clientesNaFila)
    if clientesNaFila > Espera_Y_Classe_Max[priority]:
        Espera_Y_Classe_Max[priority] = clientesNaFila
        
def updateGrafoTrabalhoResidual(servidor, time):
    global Trabalho_Residual_X, Trabalho_Residual_Y
    global Trabalho_Residual_X_Max, Trabalho_Residual_Y_Max
    Trabalho_Residual_X.append(time)
    Trabalho_Residual_X_Max = time
    if servidor != None:
        Trabalho_Residual_Y.append(servidor.clientData.getTimeRemaining())
        if servidor.clientData.getTimeRemaining() > Trabalho_Residual_Y_Max:
            Trabalho_Residual_Y_Max = servidor.clientData.getTimeRemaining()
    else:
        Trabalho_Residual_Y.append(0)
    updateGrafoTrabalhoResidualClasse(servidor,time, 0)
    updateGrafoTrabalhoResidualClasse(servidor,time, 1)
    
def updateGrafoTrabalhoResidualClasse(servidor, time, priority):
    global Trabalho_Residual_X_Classe, Trabalho_Residual_Y_Classe 
    global Trabalho_Residual_X_Classe_Max, Trabalho_Residual_Y_Classe_Max
    Trabalho_Residual_X_Classe[priority].append(time)
    Trabalho_Residual_X_Classe_Max[priority] = time
    if servidor != None:
        Trabalho_Residual_Y_Classe[priority].append(servidor.clientData.getTimeRemaining())
        if servidor.clientData.getTimeRemaining() > Trabalho_Residual_Y_Classe_Max[priority]:
            Trabalho_Residual_Y_Classe_Max[priority] = servidor.clientData.getTimeRemaining()
    else:
        Trabalho_Residual_Y_Classe[priority].append(0)
        
def getArea(X, Y):
    area = 0
    for i in range(1, len(Clientes_X)):
        dt = abs(X[i] - X[i-1])
        area += Y[i]*dt
    return area


def plotClientesSistema():
    plot(Clientes_X, Clientes_Y, Clientes_X_Max, Clientes_Y_Max)
    
def plot(x, y, x_max, y_max):
    plt.step(x, y)
    plt.axis([0, x_max, 0, y_max])
    
def plotData(xdados, y, x_max, y_max):
    plt.plot(xdados, y, 'ro')
    plt.axis([0, x_max, 0, y_max])
    plt.show()
    
def plotFunction(x, y, x_max, y_max):
    plt.plot(x, y)
    plt.axis([0, x_max, 0, y_max])
    
def clean():
    global Clientes_X, Clientes_X_Max, Clientes_Y, Clientes_Y_Max, Clientes_X_Classe
    global Clientes_X_Classe_Max, Clientes_Y_Classe, Clientes_Y_Classe_Max, Espera_X
    global Espera_X_Max, Espera_Y, Espera_Y_Max, Espera_X_Classe, Espera_X_Classe_Max
    global Espera_Y_Classe, Espera_Y_Classe_Max, Trabalho_Residual_X, Trabalho_Residual_X_Max
    global Trabalho_Residual_Y, Trabalho_Residual_Y_Max, Trabalho_Residual_X_Classe
    global Trabalho_Residual_X_Classe_Max, Trabalho_Residual_Y_Classe, Trabalho_Residual_Y_Classe_Max
        
    Clientes_X = [0]
    Clientes_X_Max = 0
    Clientes_Y = [0]
    Clientes_Y_Max = 0
    
    Clientes_X_Classe = {0: [0], 1: [0]}
    Clientes_X_Classe_Max = {0: 0, 1: 0}
    Clientes_Y_Classe = {0: [0], 1: [0]}
    Clientes_Y_Classe_Max = {0: 0, 1: 0}
    
    Espera_X = [0]
    Espera_X_Max = 0
    Espera_Y = [0]
    Espera_Y_Max = 0
    
    Espera_X_Classe = {0: [0], 1: [0]}
    Espera_X_Classe_Max = {0: 0, 1: 0}
    Espera_Y_Classe = {0: [0], 1: [0]}
    Espera_Y_Classe_Max = {0: 0, 1: 0}
    
    Trabalho_Residual_X = [0]
    Trabalho_Residual_X_Max = 0
    Trabalho_Residual_Y = [0]
    Trabalho_Residual_Y_Max = 0
    
    Trabalho_Residual_X_Classe = {0: [0], 1: [0]}
    Trabalho_Residual_X_Classe_Max = {0: 0, 1: 0}
    Trabalho_Residual_Y_Classe = {0: [0], 1: [0]}
    Trabalho_Residual_Y_Classe_Max = {0: 0, 1: 0}
