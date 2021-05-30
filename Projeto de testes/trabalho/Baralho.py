import random
import itertools

# Este bloco define a classe carta como sendo um objeto que possui os atributos cor e tipo
class Carta:
    def __init__(self, cor, tipo):
        self.cor = cor
        self.tipo = tipo

    def __str__(self):
        if (self.tipo == "+4" or self.tipo == "escolhacor"):
            return "Carta " + str(self.tipo)
        else:
            return "Carta " + str(self.tipo) + " " + str(self.cor)

    def __repr__(self):
        return self.__str__()


# Este bloco define a classe Monte (que modela a pilha de compra da partida) como sendo uma lista que possui os
# metodos desempilhaMonte, que retorna 1 carta da lista, e getMonte, que retorna toda a lista
class Monte:
    def __init__(self):
        self.CORES_VALIDAS = ["amarelo", "azul", "verde", "vermelho"]
        self.TIPOS_VALIDOS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "reverso", "pula", "escolhacor", "+4"]
        self._monte = []
        
        #Definição de cartas baseado na distribuição do Grupo2

        for cor in self.CORES_VALIDAS:
            for numero in itertools.chain(range(0, 10), range(1, 10)):
                carta_comum = Carta(cor, str(numero))
                self._monte.append(carta_comum)

        #Gerando duas cartas de cada tipo e cor
        for i in range(2):
        
            self._monte.append(Carta("amarelo", "pula"))
            self._monte.append(Carta("azul", "pula"))
            self._monte.append(Carta("verde", "pula"))
            self._monte.append(Carta("vermelho", "pula"))
        

       
            self._monte.append(Carta("amarelo", "reverso"))
            self._monte.append(Carta("azul", "reverso"))
            self._monte.append(Carta("verde", "reverso"))
            self._monte.append(Carta("vermelho", "reverso"))
        

        
            self._monte.append(Carta("amarelo", "+2"))
            self._monte.append(Carta("azul", "+2"))
            self._monte.append(Carta("verde", "+2"))
            self._monte.append(Carta("vermelho", "+2"))
            #Aninhado gera 4 Cartas especiais de cada um dos dois
            for j in range(2):
                self._monte.append(Carta("preto", "escolhacor"))
                self._monte.append(Carta("preto", "+4"))

        #Embaralhando para garantir a probabilidade
        random.shuffle(self._monte)
   

    def getMonte(self):
        temp = []
        for x in self._monte:
            temp.append(x)
        return temp

    def desempilhaMonte(self):
        return self._monte.pop()
