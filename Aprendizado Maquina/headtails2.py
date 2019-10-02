import random


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
            if jogador == adversario:
                continue
            choice = flipTheCoin()
            flip = flipTheCoin()
            if flip == choice:
                jogadores[jogador] += 100
                jogadores[adversario] -= 100
            else:
                jogadores[adversario] += 100
                jogadores[jogador] -= 100
                
            
def removeJogadoresSemRecursos(jogs):
    jogsnovo = {}
    for key in jogs:
        if jogs[key] > 0:
            jogsnovo.update({key: jogs[key]})
    return jogsnovo

def game():
    global jogadores
    jogadores = inicializa()
    jogadoresAtivos = jogadores
    for i in range(5000):
        rodada(jogadoresAtivos, 10)
        jogadoresAtivos = removeJogadoresSemRecursos(jogadoresAtivos)

    return jogadores

def inicializa():
    global jogadores
    for i in range(2500):
        jogadores.update({i:10000})
    return jogadores
