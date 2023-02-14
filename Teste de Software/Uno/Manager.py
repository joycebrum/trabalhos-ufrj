import random

LEFT = -1
RIGHT = 1

class Manager:
  n_of_players = 2
  players = []
  game_orientation = RIGHT
  buy_stack = []
  board_stack = []

  def __init__(self): 
    pass

  def checkWinner(player):
    return True if(len(player.player_cards) == 0) else False # Consertar aqui: classe Player depende do outro grupo fazer.

  def turnBoardToBuyStack():
    board_stack_top = self.board_stack.pop() 

    self.buy_stack = self.board_stack.copy()
    random.shuffle(self.buy_stack)

    self.board_stack = [board_stack_top]

  def inicializer(self, players, buy_stack, board_stack): # Consertar aqui: função inicializer depende do outro grupo fazer
    pass

  def run(self):

    while True:
      self.n_of_players = input("Digite o número de jogadores:")

      if int(self.n_of_players) not in list(range(2,10)):
          print("Número inválido de jogadores.")
      else:
          break

    for n in range(n_of_players):
      self.players.append(Player()) # Consertar aqui: classe Player depende do outro grupo fazer.

    self.inicializer(players, buy_stack, board_stack)

    start_player = random.randint(0, self.n_of_players-1)

    curr_player = start_player

    next_player = (curr_player + self.game_orientation) % self.n_of_players

    while True:
      ## Current player logic actions
      print("-----------------------------------------------")
      print("Jogador " + str(curr_player) + ", é a sua vez!")
      print("O topo da pilha da mesa é: " + board_stack[0])

      print("Suas cartas são:" + self.players[curr_player].player_cards) # Consertar aqui: classe Player depende do outro grupo fazer. Retornar uma lista printável de cartas.
      
      possible_cards_to_play = self.players[curr_player].getPossibleCardsToPlay(board_stack[0])
      print("Suas possíveis cartas a jogar são: " + possible_cards_to_play) # Consertar aqui: classe Player depende do outro grupo fazer. Retornar uma lista printável de cartas.
      
      if(not possible_cards_to_play):
        print("Você não tem cartas possíveis a jogar. Vamos comprar uma para você!")

        if(self.buy_stack < 1):
          self.turnBoardToBuyStack()
        
        self.players[curr_player].buyCard(1, self.buy_stack) # Consertar aqui: classe Player depende do outro grupo fazer.
        
        possible_cards_to_play = self.players[curr_player].getPossibleCardsToPlay(board_stack[0])
      
      if(possible_cards_to_play):
        chosen_card = int(input("Escolha qual carta irá jogar. Digite um número de 1 a " + str(len(possible_cards_to_play)) + ", que corresponde a posição da carta na listagem de possíveis cartas a jogar acima."))-1
        self.players[curr_player].playCard(possible_cards_to_play[chosen_card], self.board_stack)
      else:
        print("Você não tem cartas a jogar mesmo tendo comprado.")
      
      if(self.checkWinner(self.players[curr_player])):
        print("Jogador " + str(curr_player) + " ganhou!!! Parabéns!")
        break

      ## Manager logic actions
      # Aqui pensamos em funções que farão o efeito das ações da jogada do jogador atual nos jogadores seguintes. Além de definir quem é o próximo jogador (next_player)além de fazer curr_player = next_player.
      


manager = Manager()
manager.run()