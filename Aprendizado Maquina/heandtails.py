import random

HEAD = 'head'
TAIL = 'tail'

def flipTheCoin():
    coin = (HEAD, TAIL)
    flip = random.choice(coin)
    return flip

def game(n):
    maria = 10000
    joao = 10000
    for i in range(n):
        flip = flipTheCoin()
        if (flip == HEAD):
            if maria < 100:
                joao += maria
                maria = 0
                break
            joao += 100
            maria -= 100
        else:
            if joao < 100 :
                maria += joao
                joao = 0
                break
            joao -= 100
            maria += 100

    return maria, joao

#>>> game(5000)
#(0, 20000)
#>>> game(5000)
#(10200, 9800)
#>>> game(5000)
#(7200, 12800)
#>>> game(5000)
#(17000, 3000)
#>>> game(5000)
#(9000, 11000)
