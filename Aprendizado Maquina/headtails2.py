import random

import matplotlib.pyplot as pyplot

import numpy as np

HEAD = 'head'
TAIL = 'tail'
jogadores = dict()

def flipTheCoin():
    coin = (HEAD, TAIL)
    flip = random.choice(coin)
    return flip

def rodada(jogadoresAtivos, quant):
    global jogadores
    for jogador in jogadoresAtivos:
        for adversario in jogadoresAtivos:
            if jogador >= adversario:
                continue
            choice = HEAD
            flip = flipTheCoin()
            if flip == choice:
                jogadores[jogador] += 100
                jogadores[adversario] -= 100

            else:
                jogadores[adversario] += 100
                jogadores[jogador] -= 100
            jogadoresAtivos[jogador] = jogadores[jogador]
            jogadoresAtivos[adversario] = jogadores[adversario]


def removeJogadoresSemRecursos(jogs):
    jogsnovo = {}
    for key in jogs:
        if jogs[key] > 0:
            jogsnovo.update({key: jogs[key]})
    return jogsnovo

def inicializa(num):
    global jogadores
    for i in range(num):
        jogadores.update({i:10000})
    return jogadores

def game(n):
    global jogadores
    jogadores = inicializa(500)
    jogadoresAtivos = jogadores
    for i in range(n):
        #print("Rodada " + str(i) + " jogadores ativos: " + str(len(jogadoresAtivos)))
        rodada(jogadoresAtivos, 10)
        jogadoresAtivos = removeJogadoresSemRecursos(jogadoresAtivos)
        if (len(jogadoresAtivos)<2):
            break
        
def plot(returned) :
  x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
  y = returned

  xvals = np.linspace(0, 0.1, 1)
  yinterp = np.interp(xvals, x, y)
  pyplot.plot(x, y, 'o')
  pyplot.plot(xvals, yinterp, '-x')
  pyplot.show()

def fracaoRelativoAoMaximo(n):
    global jogadores
    game(n)
    max = 0

    for jogador in jogadores:
        if jogadores[jogador] > max:
            max = jogadores[jogador]        
    returned = [0] * 11

    for jogador in jogadores:
        val = jogadores[jogador] / max
        if val < 0.1:
            returned[0]+=1
        elif val < 0.2:
            returned[1]+=1
        elif val < 0.3:
            returned[2]+=1
        elif val < 0.4:
            returned[3]+=1
        elif val < 0.5:
            returned[4]+=1
        elif val < 0.6:
            returned[5]+=1
        elif val < 0.7:
            returned[6]+=1
        elif val < 0.8:
            returned[7]+=1
        elif val < 0.9:
            returned[8]+=1
        elif val < 1:
            returned[9]=1
        else :
            returned[10]=1

    plot(returned)
    return returned, max

fracaoRelativoAoMaximo(10000)
