import unittest
from Gerenciador import Gerenciador
from Jogador import Jogador
from Baralho import Carta

class UnitTestsFromGerenciador(unittest.TestCase):
  def setUp(self):
    self.gerenciador = Gerenciador()

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



suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestsFromGerenciador)
unittest.TextTestRunner().run(suite)


    # Given
    # When
    # Then
