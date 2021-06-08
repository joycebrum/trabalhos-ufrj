class EmptyHandException(Exception):
  pass

class InvalidGameException(Exception):
  pass

class EmptyPileException(Exception):
  pass

class InvalidCardException(Exception):
  pass

class Uno:
  def __init__(self, pile=[], top=None):
    self.pile = pile
    self.top = top

  def changeTop(self, card, cor):
    if card[0] == -4 or card[0] == -2:
      card = (card[0], cor)
    self.top = card

class UnoPlayer:
  def __init__(self, game,hand=[]):
    self.hand = hand
    self.game = game

  def buy(self):
    if len(self.game.pile) == 0:
      raise EmptyPileException("Não há cartas na pilha")
    if len(self.hand) == 0: raise EmptyHandException("Jogador não tem cartas, então não deveria estar jogando")
    card = self.game.pile.pop()
    self.hand.append(card)
    return

  def testWin(self, card):
    self.hand.remove(card)
    if len(self.hand) == 0:
      return True
    else:
      return False

  def play_card(self, card, cor):
    if not card: raise InvalidCardException("Essa carta não pode ser jogada")
    if self.hand == []:
      raise EmptyHandException("O Jogador não tem cartas para jogar")
    elif card[1] == self.game.top[1] or card[0] == self.game.top[0] or card[0] == -4 or card[0] == -2:
      self.game.changeTop(card, cor)
      return self.testWin(card)
    else:
      raise InvalidCardException("Essa carta não pode ser jogada")

  def select(self):
    can_play = []
    if len(self.hand) == 0:
      raise EmptyHandException("O Jogador não tem cartas para jogar")
    if self.game == None:
      raise InvalidGameException("Não há nenhum jogo ativo")
    if self.game.top == None:
      raise InvalidGameException("Não há carta no topo")
    for card in self.hand:
      if card[0] == self.game.top[0] or card[1] == self.game.top[1] or card[0] == -4 or card[0] == -2:
        can_play.append(card)
    return can_play