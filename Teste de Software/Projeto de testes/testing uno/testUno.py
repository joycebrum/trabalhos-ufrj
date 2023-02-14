import unittest
from Uno import Uno, UnoPlayer, EmptyHandException, InvalidCardException,EmptyPileException, InvalidGameException

class TestUnoMethods(unittest.TestCase):
  def setUp(self):
    self.game = Uno([(4, 'vermelho'), (-1, 'azul'), (-4, ''), (2, 'verde')], (6, 'amarelo'))
    self.player = UnoPlayer(self.game, [])

# Casos de Teste de 'comprar carta'
  # Caso 1 - atende o requisito {a1,b1}
  # Requisito a1 : Bloco de compras vazio
  # Requisito b1 : Jogador com 0 cartas
  # H = []
  # B = []
  def test_buy_card_empty_pile_empty_hand(self):
    self.game.pile = []
    with self.assertRaisesRegex(EmptyPileException, "^Não há cartas na pilha$"):
      self.player.buy()

  # Caso 2 - atende o requisito {a1,b2}
  # Requisito a1 : Bloco de compras vazio
  # Requisito b2 : Jogador com mais de 0 cartas
  # H = [(3, “azul”), (-4, “”)]
  # B = []
  def test_buy_card_empty_block(self):
    self.game.pile = []
    self.player.hand.append((3, 'azul'))
    self.player.hand.append((-4, ''))
    with self.assertRaisesRegex(EmptyPileException, "^Não há cartas na pilha$"):
      self.player.buy()

  # Caso 3 - atende o requisito {a2,b1}
  # Requisito a2 : Bloco de compras não vazio
  # Requisito b1 : Jogador com 0 cartas
  # H = []
  # B = [(4, “vermelho”), (-1, “azul”), (-4, “”), (2, “verde”)]
  def test_buy_card_empty_hand(self):
    with self.assertRaisesRegex(EmptyHandException, "^Jogador não tem cartas, então não deveria estar jogando$"):
      self.player.buy()

  # Caso 4 - atende o requisito {a2,b2}
  # Requisito a2 : Bloco de compras não vazio
  # Requisito b2 : Jogador com mais de 0 cartas
  # H = [(5, “verde”), (-1, “vermelho”)]
  # B = [(4, “vermelho”), (-1, “azul”), (-4, “”), (2, “verde”)]
  def test_buy_card(self):
    self.player.hand = [(5, 'verde'), (-1, 'vermelho')]
    self.player.buy()
    self.assertEqual(3, len(self.player.hand))
    self.assertIn((2, 'verde'), self.player.hand)

# Casos de teste 'jogar carta'
  # Caso 1 - atende o requisito {a1,b2,c3,d2}
  # Requisito a1 : Carta válida pode ser jogada
  # Requisito b2 : Flag de carta especial desativada
  # Requisito c3 : mais de 1 carta de mão
  # Requisito d2 : Não mudar a cor do topo com especial
  # H = [(3, “azul”), (5, “amarelo”), (6, “verde”)]
  # C = (6, “verde”)
  # T = (6, “amarelo”)
  # F = false
  # color = null
  def test_play_card_1(self):
    self.player.hand = [(3, 'azul'), (5, 'amarelo'), (6, 'verde')]
    won = self.player.play_card((6, 'verde'), None)
    self.assertEqual(self.game.top, (6, 'verde'))
    self.assertFalse(won)

  # Caso 2 - atende o requisito {a1,b2,c3,d1}
  # Requisito a1 : Carta válida pode ser jogada
  # Requisito b2 : Flag de carta especial desativada
  # Requisito c3 : mais de 1 carta de mão
  # Requisito d1 : Mudar a cor do topo com especial
  # H = [(-1, “azul”), (5, “verde”), (9, “verde”), (-2, “”)]
  # C = (-2, “”)
  # T = (6, “amarelo”)
  # F = false
  # color = “verde”
  def test_play_card_2(self):
    self.player.hand = [(-1, 'azul'), (5, 'verde'), (9, 'verde'), (-2, '')]
    won = self.player.play_card((-2, ''), 'verde')
    self.assertEqual(self.game.top, (-2, 'verde'))
    self.assertFalse(won)

  # Caso 3 - atende o requisito {a1,b2,c1,d2}
  # Requisito a1 : Carta válida pode ser jogada
  # Requisito b2 : Flag de carta especial desativada
  # Requisito c1 : 0 cartas na mão
  # Requisito d2 : Não mudar a cor do topo com especial
  # H = []
  # C = (3, “amarelo”)
  # T = (7, “amarelo”)
  # F = false
  # color = null
  def test_play_card_3(self):
    self.player.hand = []
    self.game.top = (3, 'amarelo')
    with self.assertRaisesRegex(EmptyHandException, "^O Jogador não tem cartas para jogar$"):
      self.player.play_card((7, 'amarelo'), None)


  # Caso 4 - atende o requisito {a1,b2,c2,d2}
  # Requisito a1 : Carta válida pode ser jogada
  # Requisito b2 : Flag de carta especial desativada
  # Requisito c2 : 1 carta na mão
  # Requisito d2 : Não mudar a cor do topo com especial
  # H = [(3, “amarelo”)]
  # C = (3, “amarelo”)
  # T = (8, “amarelo”)
  # F = false
  # color = null
  def test_play_card_4(self):
    self.player.hand = [(3, 'amarelo')]
    self.game.top = (8, 'amarelo')
    won = self.player.play_card((3, 'amarelo'), None)
    self.assertEqual(self.game.top, (3, 'amarelo'))
    self.assertTrue(won)

  # Caso 5 - atende o requisito {a1,b1,c3,d2}
  # Requisito a1 : Carta válida pode ser jogada
  # Requisito b1 : Flag de carta especial ativada
  # Requisito c3 : mais de 1 carta de mão
  # Requisito d2 : Não mudar a cor do topo com especial
  # H = [(3, “azul”), (5, “amarelo”), (-3, “amarelo”)]
  # C = (-3, “amarelo”)
  # T = (-3, “amarelo”)
  # F = true
  # color = null
  def test_play_card_5(self):
    self.player.hand = [(3, 'azul'), (-3, 'amarelo')]
    self.game.top = (-3, 'amarelo')
    won = self.player.play_card((-3, 'amarelo'), None)
    self.assertEqual(self.game.top, (-3, 'amarelo'))
    self.assertFalse(won)


  # Caso 6 - atende o requisito {a2,b2,c3,d2}
  # Requisito a2 : Carta válida não pode ser jogada
  # Requisito b2 : Flag de carta especial desativada
  # Requisito c3 : mais de 1 carta de mão
  # Requisito d2 : Não mudar a cor do topo com especial
  # H = [(3, “azul”), (5, “amarelo”), (6, “verde”)]
  # C = (6, “verde”)
  # T = (5, “vermelho”)
  # F = false
  # color = null
  def test_play_card_6(self):
    self.player.hand = [(3, 'azul'), (5, 'amarelo'), (6, 'verde')]
    self.game.top = (5, 'vermelho')
    with self.assertRaisesRegex(InvalidCardException, "^Essa carta não pode ser jogada$"):
      self.player.play_card((6, 'verde'), None)

  # Caso 7 - atende o requisito {a3,b2,c3,d2}
  # Requisito a3 : Carta nula
  # Requisito b2 : Flag de carta especial desativada
  # Requisito c3 : mais de 1 carta de mão
  # Requisito d2 : Não mudar a cor do topo com especial
  # H = [(3, “azul”), (5, “amarelo”), (6, “vermelho”)]
  # C = null
  # T = (6, “vermelho”)
  # F = false
  # color = null
  def test_play_card_7(self):
    self.player.hand = [(3, 'azul'), (5, 'amarelo'), (6, 'vermelho')]
    self.game.top = (6, 'vermelho')
    with self.assertRaisesRegex(InvalidCardException, '^Essa carta não pode ser jogada$'):
      self.player.play_card(None, None)


  # Caso 8 - atende o requisito {a4,b2,c3,d2}
  # Requisito a4 : Carta inválida
  # Requisito b2 : Flag de carta especial desativada
  # Requisito c3 : mais de 1 carta de mão
  # Requisito d2 : Não mudar a cor do topo com especial
  # H = [(3, “azul”), (7, “azul”), (5, “amarelo”)]
  # C = (15, “dourado”)
  # T = (5, “amarelo”)
  # F = false
  # color = null
  def test_play_card_8(self):
    self.player.hand = [(3, 'azul'), (7, 'azul'), (5, 'amarelo')]
    self.game.top = (5, 'amarelo')
    with self.assertRaisesRegex(InvalidCardException, '^Essa carta não pode ser jogada$'):
      self.player.play_card((15, 'dourado'), None)


# Casos de teste 'selecionar carta'
  # Caso 1 - atende o requisito {a1,b1,c1,d1,e1,f2}
  # Requisito a1 : 0 cartas normais na mão com a mesma cor do topo
  # Requisito b1 : 0 cartas normais na mão com mesmo número que o do topo
  # Requisito c1 : 0 cartas na mão +4 ou coringa
  # Requisito d1 : 0 cartas especiais de mesma cor do topo
  # Requisito e1 : 0 cartas especiais de mesmo número do topo
  # Requisito f2 : mais de 0 cartas que não podem ser jogadas
  # H = [(3, “azul”)]
  # T = (5, “verde”)
  def test_select_1(self):
    self.player.hand = [(3, 'azul')]
    self.game.top = (5, 'amarelo')
    slc = self.player.select()
    self.assertEqual(slc, [])

  # Caso 2 - atende o requisito {a1,b1,c1,d1,e1,f1}
  # Requisito a1 : 0 cartas normais na mão com a mesma cor do topo
  # Requisito b1 : 0 cartas normais na mão com mesmo número que o do topo
  # Requisito c1 : 0 cartas na mão +4 ou coringa
  # Requisito d1 : 0 cartas especiais de mesma cor do topo
  # Requisito e1 : 0 cartas especiais de mesmo número do topo
  # Requisito f1 : 0 cartas que não podem ser jogadas
  # H = []
  # T = (5, “verde”)
  def test_select_2(self):
    self.player.hand = []
    self.game.top = (5, 'amarelo')
    with self.assertRaisesRegex(EmptyHandException, "^O Jogador não tem cartas para jogar$"):
      slc = self.player.select()


  # Caso 3 - atende o requisito {a1,b1,c1,d1,e2,f2}
  # Requisito a1 : 0 cartas normais na mão com a mesma cor do topo
  # Requisito b1 : 0 cartas normais na mão com mesmo número que o do topo
  # Requisito c1 : 0 cartas na mão +4 ou coringa
  # Requisito d1 : 0 cartas especiais de mesma cor do topo
  # Requisito e2 : mais de 0 cartas especiais de mesmo número do topo
  # Requisito f2 : mais de 0 cartas que não podem ser jogadas
  # H = [(-1, “vermelho”), (3, “verde”), (7, “azul”)]
  # T = (-1, “amarelo”)
  def test_select_3(self):
    self.player.hand = [(-1, 'vermelho'), (3, 'verde'), (7, 'azul')]
    self.game.top = (-1, 'amarelo')
    slc = self.player.select()
    self.assertEqual(slc, [(-1, 'vermelho')])

  # Caso 4 - atende o requisito {a1,b1,c1,d2,e1,f2}
  # Requisito a1 : 0 cartas normais na mão com a mesma cor do topo
  # Requisito b1 : 0 cartas normais na mão com mesmo número que o do topo
  # Requisito c1 : 0 cartas na mão +4 ou coringa
  # Requisito d2 : mais de 0 cartas especiais de mesma cor do topo
  # Requisito e1 : 0 cartas especiais de mesmo número do topo
  # Requisito f2 : mais de 0 cartas que não podem ser jogadas
  # H = [(1, “verde”), (6, “azul”), (-3, “vermelho”)]
  # T = (-5, “vermelho”)
  def test_select_4(self):
    self.player.hand = [(1, 'verde'), (6, 'azul'), (-3, 'vermelho')]
    self.game.top = (-5, 'vermelho')
    slc = self.player.select()
    self.assertEqual(slc, [(-3, 'vermelho')])

  # Caso 5 - atende o requisito {a1,b1,c2,d1,e1,f2}
  # Requisito a1 : 0 cartas normais na mão com a mesma cor do topo
  # Requisito b1 : 0 cartas normais na mão com mesmo número que o do topo
  # Requisito c2 : mais de 0 cartas na mão +4 ou coringa
  # Requisito d1 : 0 cartas especiais de mesma cor do topo
  # Requisito e1 : 0 cartas especiais de mesmo número do topo
  # Requisito f2 : mais de 0 cartas que não podem ser jogadas
  # H = [(-2, “”), (3, “verde”), (-4, “”), (5, “vermelho”)]
  # T = (1, “azul”)
  def test_select_5(self):
    self.player.hand = [(-2, ''), (3, 'verde'), (-4, ''), (5, 'vermelho')]
    self.game.top = (1, 'azul')
    slc = self.player.select()
    self.assertEqual(slc, [(-2, ''), (-4, '')])

  # Caso 6 - atende o requisito {a1,b2,c1,d1,e1,f2}
  # Requisito a1 : 0 cartas normais na mão com a mesma cor do topo
  # Requisito b2 : mais de 0 cartas normais na mão com o mesmo número do topo
  # Requisito c1 : 0 cartas na mão +4 ou coringa
  # Requisito d1 : 0 cartas especiais de mesma cor do topo
  # Requisito e1 : 0 cartas especiais de mesmo número do topo
  # Requisito f2 : mais de 0 cartas que não podem ser jogadas
  # H = [(6, “vermelho”), (3, “azul”), (2, “amarelo”), (6, “vermelho”)]
  # T = (6, “verde”)
  def test_select_6(self):
    self.player.hand = [(6, 'vermelho'), (3, 'azul'), (2, 'amarelo'), (6, 'vermelho')]
    self.game.top = (6, 'verde')
    slc = self.player.select()
    self.assertEqual(slc, [(6, 'vermelho'), (6, 'vermelho')])


  # Caso 7 - atende o requisito {a2,b1,c1,d1,e1,f2}
  # Requisito a2 : mais de 0 cartas normais na mão com a mesma cor do topo
  # Requisito b1 : 0 cartas normais na mão com mesmo número que o do topo
  # Requisito c1 : 0 cartas na mão +4 ou coringa
  # Requisito d1 : 0 cartas especiais de mesma cor do topo
  # Requisito e1 : 0 cartas especiais de mesmo número do topo
  # Requisito f2 : mais de 0 cartas que não podem ser jogadas
  # H = [(9, “amarelo”), (1, “amarelo”), (2, “amarelo”), (2, “vermelho”)]
  # T = (-1, “amarelo”)
  def test_select_7(self):
    self.player.hand = [(9, 'amarelo'), (1, 'amarelo'), (2, 'amarelo'), (2, 'vermelho')]
    self.game.top = (-1, 'amarelo')
    slc = self.player.select()
    self.assertEqual(slc, [(9, 'amarelo'), (1, 'amarelo'), (2, 'amarelo')])


  # Caso para eliminar mutação referente a mudar a cor do topo com +4
  def test_mutation_plus4(self):
    self.player.hand = [(-1, 'azul'), (5, 'verde'), (9, 'verde'), (-4, '')]
    self.player.play_card((-4, ''), 'azul')
    self.assertEqual(self.game.top, (-4, 'azul'))

  # Caso para eliminar mutação referente ao InvalidGameException
  def test_mutation_no_game(self):
    self.player.hand = [(-1, 'azul'), (5, 'verde'), (9, 'verde')]
    self.player.game = None
    with self.assertRaisesRegex(InvalidGameException, "^Não há nenhum jogo ativo$"):
      self.player.select()

   # Caso para eliminar mutação referente ao InvalidGameException
  def test_mutation_no_card(self):
    self.player.hand = [(-1, 'azul'), (5, 'verde'), (9, 'verde')]
    self.player.game.top = None
    with self.assertRaisesRegex(InvalidGameException, "^Não há carta no topo$"):
      self.player.select()
suite = unittest.TestLoader().loadTestsFromTestCase(TestUnoMethods)
unittest.TextTestRunner().run(suite)