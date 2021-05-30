import random
from Baralho import Carta
from Baralho import Monte
from Jogador import Jogador

class Gerenciador:

  def __init__(self):
    self.ESQUERDA = -1
    self.DIREITA = 1
    self.TERMINAROJOGO = False
    self.n_de_jogadores = 2
    self.jogadores = []
    self.orientacao_jogo = self.DIREITA
    self.pilha_compra = []
    self.pilha_mesa = []
    self.jogou_carta_preta = False
    self.qtd_cartas_iniciais = 7

  def verificarVencedor(self, jogador):
    """
        Verifica se o jogador venceu, ou seja, se ele não possui mais cartas em mãos.
        :param jogador: Objeto do tipo Jogador.
        :return: Booleano
    """
    return True if(len(jogador.cartas) == 0) else False # Consertar aqui: classe Player depende do outro grupo fazer.

  def virarPilhaMesaParaCompra(self):
    """
        Transforma a pilha de cartas da mesa na pilha de compra. As cartas são embaralhadas.
    """

    topo_pilha_mesa = self.pilha_mesa.pop()

    self.pilha_compra = self.pilha_mesa.copy()
    random.shuffle(self.pilha_compra)

    self.pilha_mesa = [topo_pilha_mesa]

  def calcularProxJogador(self, atual_jogador, jogou_carta_especial=False, jogou_reverso=False, jogou_escolhacor=False):
    """
        Calcula o próximo jogador baseado no que foi jogado pelo atual.
        :param atual_jogador: Posição na lista do atual jogador.
        :param jogou_carta_especial: Booleano que indica se o atual jogador jogou uma carta especial.
        :param jogou_reverso: Booleano que indica se o atual jogador jogou uma carta reverso.
        :return Posição na lista do próximo jogador
    """
    if (not jogou_carta_especial): # Cartas de números
      return (atual_jogador + self.orientacao_jogo) % self.n_de_jogadores

    elif (jogou_carta_especial and jogou_reverso) or (jogou_carta_especial and jogou_escolhacor): # Carta reverso ou carta escolha cor
      return (atual_jogador + self.orientacao_jogo) % self.n_de_jogadores
    
    else: # Cartas especiais que não são reverso
      return (atual_jogador + 2*self.orientacao_jogo) % self.n_de_jogadores

  def inicializarJogo(self):
    """
        Inicializa o jogo: cria as cartas e as distribui para os jogadores e as pilhas.
    """
    # Inicializa a pilha de descarte do jogo construindo o objeto "monte" e retirando 1 carta
    monte = Monte()

    while True:
      primeira_carta = monte.desempilhaMonte()
      self.pilha_mesa.append(primeira_carta)
      if primeira_carta.tipo != "+2" and primeira_carta.tipo != "reverso" and primeira_carta.tipo != "pula" and primeira_carta.tipo != "escolhacor" and primeira_carta.tipo != "+4":
        break


    while True:
      self.n_de_jogadores = int(input("Digite o número de jogadores:"))

      if int(self.n_de_jogadores) not in list(range(2,10)):
        print("Número inválido de jogadores.")
      else:
        break

    # Inicializa cada jogador com sua respectiva quantidade de cartas
    for i in range(self.n_de_jogadores):
        listaMao = []
        for j in range(self.qtd_cartas_iniciais):
          listaMao.append(monte.desempilhaMonte())
        jogador = Jogador(listaMao)
        self.jogadores.append(jogador)

    # Inicializa a pilha de compra do jogo retirando as cartas restantes do objeto "monte"
    self.pilha_compra = monte.getMonte().copy()

  def acaoJogada(self, atual_jogador, carta):
    prox_jogador = self.calcularProxJogador(atual_jogador, False, False, False)

    if carta.tipo == "+2":
      self.jogadores[prox_jogador].comprar(2, self.pilha_compra)
      print("Jogador " + str(prox_jogador) + "comprou 2 cartas!")
      print("Suas cartas são: " + str(self.jogadores[prox_jogador].cartas))

      prox_jogador = self.calcularProxJogador(atual_jogador, True, False, False)

    elif carta.tipo == "reverso":
      self.orientacao_jogo = self.ESQUERDA if (self.orientacao_jogo == self.DIREITA) else self.DIREITA
      print("O jogo virou de sentido!")

      prox_jogador = self.calcularProxJogador(atual_jogador, True, True, False)

    elif carta.tipo == "pula":
      print("Jogador " + str(prox_jogador) + "foi pulado!")

      prox_jogador = self.calcularProxJogador(atual_jogador, True, False, False)

    elif carta.tipo == "escolhacor":
      cor = self.jogadores[atual_jogador].escolher_cor_de_coringa()
      carta.cor = cor
      prox_jogador = self.calcularProxJogador(atual_jogador, True, False, True)

    elif carta.tipo == "+4":
      self.jogadores[prox_jogador].comprar(4, self.pilha_compra)
      print("Jogador " + str(prox_jogador) + " comprou 4 cartas!")
      print("Suas cartas são: " + str(self.jogadores[prox_jogador].cartas))

      prox_jogador = self.calcularProxJogador(atual_jogador, True, False, False)
      cor = self.jogadores[atual_jogador].escolher_cor_de_coringa()
      carta.cor = cor
      

    return prox_jogador

  def gerenciarJogo(self):
    """
        Gerencia o jogo: chama as funções do jogador e faz o efeito de suas ações, dá a vez para o próximo jogador.
        Nesta lógica, as variáveis primeiro_jogador, atual_jogador e prox_jogador indicam a posição do objeto Jogador na lista jogadores.
    """
    self.inicializarJogo()

    primeiro_jogador = random.randint(0, self.n_de_jogadores-1)

    atual_jogador = primeiro_jogador

    while not self.TERMINAROJOGO:
      
      #### Código das ações do jogador atual ####
      
      print("-----------------------------------------------")
      print("Jogador " + str(atual_jogador) + ", é a sua vez!")
      print("O topo da pilha da mesa é: " + str(self.pilha_mesa[0]))

      print("Suas cartas são: " + str(self.jogadores[atual_jogador].cartas))
      
      possiveis_cartas_para_jogar = self.jogadores[atual_jogador].selecionar(self.pilha_mesa[0])
      print("Suas possíveis cartas a jogar são: " + str(possiveis_cartas_para_jogar))
      
      # Caso o jogador não tenha cartas para jogar, o gerente compra uma para ele. Caso a pilha de compra esteja vazia, a pilha de mesa
      # vira a de compra antes de passar uma carta para o jogador atual.
      if(not possiveis_cartas_para_jogar):
        print("---------------------")
        print("Você não tem cartas possíveis a jogar. Vamos comprar uma para você!")

        if(len(self.pilha_compra) < 1):
          self.virarPilhaMesaParaCompra() # Caso a pilha de compra esteja vazia, a pilha de mesa será embaralhada e virará a de compra.
        
        self.jogadores[atual_jogador].comprar(1, self.pilha_compra)
        
        possiveis_cartas_para_jogar = self.jogadores[atual_jogador].selecionar(self.pilha_mesa[0])
        print("Suas cartas agora são: " + str(self.jogadores[atual_jogador].cartas))
        print("Suas possíveis cartas a jogar agora são: " + str(possiveis_cartas_para_jogar))

      # Verifica se agora tem cartas a jogar e caso sim, o jogador joga, caso contrário ele é dado a vez ao próximo.
      if(possiveis_cartas_para_jogar):
        carta_escolhida = int(input("Escolha qual carta irá jogar. Digite um número de 1 a " + str(len(possiveis_cartas_para_jogar)) + ", que corresponde a posição da carta na listagem de possíveis cartas a jogar acima."))-1
        prox_jogador = self.acaoJogada(atual_jogador, possiveis_cartas_para_jogar[carta_escolhida])

        self.jogadores[atual_jogador].jogar(possiveis_cartas_para_jogar[carta_escolhida], self.pilha_mesa)

      else:
        print("Você não tem cartas a jogar mesmo tendo comprado uma nova. Por isso a vez será passada.")
        atual_jogador = self.calcularProxJogador(atual_jogador)
        continue
      
      # Verifica se o jogador atual é o vencedor. Caso seja, acaba o jogo.
      if(self.verificarVencedor(self.jogadores[atual_jogador])):
        self.TERMINAROJOGO = True
        print("-----------------------------------------------")
        print("-----------------------------------------------")
        print("Jogador " + str(atual_jogador) + " ganhou!!! Parabéns!")
        break
      
      atual_jogador = prox_jogador
     
if __name__ == "__main__":
  gerenciador = Gerenciador()
  gerenciador.gerenciarJogo()
