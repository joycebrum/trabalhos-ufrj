'''
Feito por Joyce Brum e Thiago Outeiro
formato de entrada:
    estados -> array de strings, onde cada string representa o nome de um estado
    relacoes -> mapa de mapas onde:
                    chave: tipo (agente)
                    valor é o mapa:
                        chave: estado "s" - string
                        valor: array de estados - string - vizinhos de "s"
    valoracao -> mapa que indica a valoração do grafo;
                    chave: variáveis (proposições) - string
                    valor: array de estados - strings - nos quais a proposição é verdadeira
    f -> formula a ser avaliada - string
'''

from parserModule import transformaFormula
from constant import W
from constant import R 
from constant import V 
from constant import funcao
from processaEntrada import execute
from processaEntrada import montaValoracaoLocal
import constant
    

def valor(estados, relacoes, valoracao, estado, f):
    global W, R, V
    W, R, V = estados, relacoes, valoracao
    return verifica(estado, f)

#rode esse com f = "" para rodar o caso default especificado em constant.h
def verifica(estado, f):
    global funcao
    if f:
        funcao = f
    mapa = montaValoracaoLocal(estado)
    if estado:
        formula = transformaFormula(funcao)
        print(formula)
        return execute(estado, formula, mapa)
    else :
        return "erro, entrada inválida";
    
