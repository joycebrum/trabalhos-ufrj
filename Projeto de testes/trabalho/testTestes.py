import unittest
from unittest import mock
from Gerenciador import Gerenciador
from Jogador import Jogador
from Baralho import Carta
from Baralho import Monte
from random import randint
from unittest.mock import patch

class UnitTestsFromGerenciador(unittest.TestCase):
  def setUp(self):
    self.gerenciador = Gerenciador()
    self.monte = Monte()

  def hand_consistent(self, before, after):
    for card in before:
      if card not in after:
        return False
    return True

#test verificarVencedor
  def test_winner(self):
    # Given
    jogador = Jogador([])

    # When
    ganhou = self.gerenciador.verificarVencedor(jogador)

    # Then
    self.assertTrue(ganhou)

  def test_not_winner(self):
    # Given
    jogador = Jogador([Carta("vermelho", "1")])

    # When
    ganhou = self.gerenciador.verificarVencedor(jogador)

    # Then
    self.assertFalse(ganhou)
#test virarPilhaMesaParaCompra
  def test_turn_stack(self) :
    # Given
    self.gerenciador.pilha_mesa = self.monte.getMonte()
    self.gerenciador.pilha_compra = []

    # When
    cards = self.gerenciador.pilha_mesa.copy()
    topo = cards.pop()
    self.gerenciador.virarPilhaMesaParaCompra()

    testCards = True
    for card in cards:
      if card in self.gerenciador.pilha_compra:
        continue
      else:
        testCards = False
        break

    # Then
    self.assertEqual(len(self.gerenciador.pilha_mesa), 1)
    self.assertEqual(self.gerenciador.pilha_mesa[0].cor, topo.cor)
    self.assertEqual(self.gerenciador.pilha_mesa[0].tipo, topo.tipo)
    self.assertEqual(len(cards), len(self.gerenciador.pilha_compra))
    self.assertTrue(testCards)
#test calcularProxJogador
  def test_next_player_default_esquerda(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 2
    expectedNextPlayer = (player - 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,False, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_default_direita(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 2
    expectedNextPlayer = (player + 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,False, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_default_esquerda_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 0
    expectedNextPlayer = (player - 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,False, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_default_direita_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 4
    expectedNextPlayer = (player + 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,False, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)


  def test_next_player_special_reverse_direita(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 2
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player + 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, True, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_reverse_esquerda(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 2
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player - 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, True, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_reverse_direita_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 4
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player + 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, True, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_reverse_esquerda_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 0
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player - 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, True, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)


  def test_next_player_special_chose_color_direita(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 2
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player + 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, True)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_chose_color_esquerda(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 2
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player - 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, True)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_chose_color_direita_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 4
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player + 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, True)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_chose_color_esquerda_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 0
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player - 1) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, True)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)


  def test_next_player_special_other_direita(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 2
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player + 2) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_other_esquerda(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 2
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player - 2) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_other_direita_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.DIREITA

    # When
    player = 4
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player + 2) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)

  def test_next_player_special_other_esquerda_final(self):
    # Given
    self.gerenciador.n_de_jogadores = 5
    self.gerenciador.orientacao_jogo = self.gerenciador.ESQUERDA

    # When
    player = 0
    orientacao = self.gerenciador.orientacao_jogo
    expectedNextPlayer = (player - 2) % self.gerenciador.n_de_jogadores
    nextPlayer = self.gerenciador.calcularProxJogador(player,True, False, False)

    # Then
    self.assertEqual(nextPlayer, expectedNextPlayer)
#test inicializarJogo
  @mock.patch("Gerenciador.input", create = True)
  def test_inicialzar_jogo(self, mocked_input):
    # Given
    mocked_input.side_effect = ["4"]
    # When
    self.gerenciador.inicializarJogo()

    checkFirstCardType = True
    firstCardType = self.gerenciador.pilha_mesa[-1].tipo
    if(firstCardType == "+2" or firstCardType == "reverso" or firstCardType == "pula" or firstCardType == "escolhacor" or firstCardType == "+4"):
      checkFirstCardType = False

    checkPlayersHands = True
    for jogador in self.gerenciador.jogadores:
      if len(jogador.cartas) == self.gerenciador.qtd_cartas_iniciais:
        continue
      else:
        checkPlayersHands = False
        break

    # Then
    self.assertTrue(len(self.gerenciador.pilha_compra) != 0)
    self.assertTrue(len(self.gerenciador.pilha_mesa) > 0)
    self.assertTrue(checkFirstCardType)
    self.assertTrue(checkFirstCardType)

  @mock.patch("Gerenciador.input", create = True)
  def test_inicialzar_jogo_wrong_number_of_players(self, mocked_input):
    # Given
    mocked_input.side_effect = ["1", "1", "4"]
    # When
    self.gerenciador.inicializarJogo()

    checkFirstCardType = True
    firstCardType = self.gerenciador.pilha_mesa[-1].tipo
    if(firstCardType == "+2" or firstCardType == "reverso" or firstCardType == "pula" or firstCardType == "escolhacor" or firstCardType == "+4"):
      checkFirstCardType = False

    checkPlayersHands = True
    for jogador in self.gerenciador.jogadores:
      if len(jogador.cartas) == self.gerenciador.qtd_cartas_iniciais:
        continue
      else:
        checkPlayersHands = False
        break

    # Then
    self.assertTrue(len(self.gerenciador.pilha_compra) != 0)
    self.assertTrue(len(self.gerenciador.pilha_mesa) > 0)
    self.assertTrue(checkFirstCardType)
    self.assertTrue(checkFirstCardType)
#test açãoJogada
  @mock.patch("builtins.input", create = True)
  def test_play_plus_two(self, mocked_input):
    # Given
    mocked_input.side_effect = ["4"]
    self.gerenciador.inicializarJogo()
    actualPlayer = 0
    buyingPlayer = 1
    direction = self.gerenciador.orientacao_jogo
    buyingPlayerHandBeforeBuy = self.gerenciador.jogadores[buyingPlayer].cartas.copy()
    # When
    carta = Carta("Vermelho", "+2")
    next_player = self.gerenciador.acaoJogada(actualPlayer, carta)
    buyingPlayerHandAfterBuy = self.gerenciador.jogadores[buyingPlayer].cartas.copy()

    # Then
    self.assertEqual(len(buyingPlayerHandBeforeBuy)+2, len(buyingPlayerHandAfterBuy))
    self.assertTrue(self.hand_consistent(buyingPlayerHandBeforeBuy, buyingPlayerHandAfterBuy))
    self.assertEqual(self.gerenciador.orientacao_jogo, direction)
    self.assertEqual(next_player, (actualPlayer + 2*direction) % self.gerenciador.n_de_jogadores)

  @patch("builtins.input", side_effect=['4', 'verde'])
  def test_play_plus_four(self, mocked_input):
    # Given
    self.gerenciador.inicializarJogo()
    actualPlayer = 0
    buyingPlayer = 1
    direction = self.gerenciador.orientacao_jogo
    buyingPlayerHandBeforeBuy = self.gerenciador.jogadores[buyingPlayer].cartas.copy()
    # When
    carta = Carta("preto", "+4")
    next_player = self.gerenciador.acaoJogada(actualPlayer, carta)
    buyingPlayerHandAfterBuy = self.gerenciador.jogadores[buyingPlayer].cartas.copy()

    # Then
    self.assertEqual(len(buyingPlayerHandBeforeBuy)+4, len(buyingPlayerHandAfterBuy))
    self.assertTrue(self.hand_consistent(buyingPlayerHandBeforeBuy, buyingPlayerHandAfterBuy))
    self.assertEqual(self.gerenciador.orientacao_jogo, direction)
    self.assertEqual(next_player, (actualPlayer + 2*direction) % self.gerenciador.n_de_jogadores)
    self.assertEqual(carta.cor, "verde")

  @patch("builtins.input", side_effect=['4'])
  def test_play_reverse(self, mocked_input):
    # Given
    self.gerenciador.inicializarJogo()
    actualPlayer = 0
    direction = self.gerenciador.orientacao_jogo
    # When
    carta = Carta("azul", "reverso")
    next_player = self.gerenciador.acaoJogada(actualPlayer, carta)

    # Then
    self.assertEqual(self.gerenciador.orientacao_jogo, -direction)
    self.assertEqual(next_player, (actualPlayer - direction) % self.gerenciador.n_de_jogadores)

  @patch("builtins.input", side_effect=['4'])
  def test_play_block(self, mocked_input):
    # Given
    self.gerenciador.inicializarJogo()
    actualPlayer = 0
    direction = self.gerenciador.orientacao_jogo
    # When
    carta = Carta("azul", "pula")
    next_player = self.gerenciador.acaoJogada(actualPlayer, carta)

    # Then
    self.assertEqual(self.gerenciador.orientacao_jogo, direction)
    self.assertEqual(next_player, (actualPlayer + 2*direction) % self.gerenciador.n_de_jogadores)

  @patch("builtins.input", side_effect=['4', 'azul'])
  def test_play_chose(self, mocked_input):
    # Given
    self.gerenciador.inicializarJogo()
    actualPlayer = 0
    direction = self.gerenciador.orientacao_jogo

    # When
    carta = Carta("preto", "escolhacor")
    next_player = self.gerenciador.acaoJogada(actualPlayer, carta)

    # Then
    self.assertEqual(self.gerenciador.orientacao_jogo, direction)
    self.assertEqual(next_player, (actualPlayer + direction) % self.gerenciador.n_de_jogadores)
    self.assertEqual(carta.cor, "azul")

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestsFromGerenciador)
unittest.TextTestRunner().run(suite)


    # Given
    # When
    # Then
