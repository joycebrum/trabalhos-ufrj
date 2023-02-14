
from constant import W
from constant import R 
from constant import V 
from constant import funcao
import constant

def execute(estado, formula, mapa):
    if isinstance(formula, str):
        return mapa[formula]
    elif isinstance(formula, bool):
        return formula
    else:
        i = 0
        while i < len(formula):
            if formula[i] == constant.NOT:
                valor = execute(estado, formula[i+1], mapa)
                formula.pop(i+1)
                formula[i] = not valor
            else :
                i = i + 1
        i=0
        while i < len(formula):
            if formula[i] == constant.PARATODOINICIO:
                tipo = formula[i+1]
                valor = paraTodoVizinho(tipo, estado, formula[i+3])
                formula.pop(i+3)
                formula.pop(i+2)
                formula.pop(i+1)
                formula[i] = valor
            else:
                 i = i + 1
        i = 0
        while i < len(formula):
            if formula[i] == constant.ALGUMINICIO:
                tipo = formula[i+1]
                valor = existeAlgumVizinho(tipo, estado, formula[i+3])
                formula.pop(i+3)
                formula.pop(i+2)
                formula.pop(i+1)
                formula[i] = valor
            else:
                 i = i + 1
        i = 0
        while i < len(formula) :
            if formula[i] == constant.AND or formula[i] == constant.OR:
                
                valorEsquerdo = execute(estado, formula[i-1], mapa)
                valorDireito = execute(estado, formula[i+1], mapa)
                if formula[i] == constant.AND:
                    formula[i] = valorEsquerdo and valorDireito
                else:
                    formula[i] = valorEsquerdo or valorDireito
                    
                formula.pop(i+1)
                formula.pop(i-1)
                i=i-2
            i = i + 1
        i = 0
        while i < len(formula) :
            if formula[i] == constant.IMPLICACAO :
                valorEsquerdo = execute(estado, formula[i-1], mapa)
                valorDireito = execute(estado, formula[i+1], mapa)
                formula[i] = (not valorEsquerdo) or valorDireito
                formula.pop(i+1)
                formula.pop(i-1)
                i=i-2
            i=i+1
        return execute(estado, formula[0], mapa)

#W array com nome dos estados
# R mapa com as relacoes entre os estados
# V mapa com as valoracoes (estado w pertence a V[p])
def montaValoracaoLocal(estado):
    global V
    valoracaoLocal = {}
    for variavel, estados in V.items():
        valoracaoLocal[variavel] = valoracao(variavel, estado, V)
    return valoracaoLocal

def existeAlgumVizinho(tipo, estado, formula):
    global W, R, V
    
    if not tipo in R or not estado in R[tipo]:
        return False #Sumidouro
    
    for vizinho in R[tipo][estado]:
        valoracaoLocal = montaValoracaoLocal(vizinho)
        if isinstance(formula, str):
            formulaSave = '' + formula
        elif isinstance(formula, bool):
            formulaSave = formula
        else:
            formulaSave = [] + formula
        if execute(vizinho, formulaSave, valoracaoLocal):
            return True
    return False

def paraTodoVizinho(tipo, estado, formula):
    global W, R, V
    if not tipo in R or not estado in R[tipo]:
        return True #Sumidouro
    
    for vizinho in R[tipo][estado]:
        valoracaoLocal = montaValoracaoLocal(vizinho)
        if isinstance(formula, str):
            formulaSave = '' + formula
        elif isinstance(formula, bool):
            formulaSave = formula
        else:
            formulaSave = [] + formula
        if not execute(vizinho, formulaSave, valoracaoLocal):
            return False
    return True
        

# p é verdadeiro no estado w - true, se não, false
def valoracao(p, w, V):
    for estado in V[p]:
        if estado == w:
            return True
    return False

# se w2 é vizinho de w1
def ehVizinho(w1, R, tipo, w2):
    if not tipo in R:
        return False
    for vizinho in R[tipo][w1]:
        if vizinho == w2:
            return True

    return False
