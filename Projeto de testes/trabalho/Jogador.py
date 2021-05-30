"""
Grupo 01 - Trabalho UNO - Projeto de Teste 2020.2
Jones Martins - DRE: 115149195
Felipe Menescal - DRE: 113282298
Larissa Galeno - DRE: 116083017
Leonardo Gonçalves - DRE: 111337097
"""

import itertools
from collections import deque
import enum
import typing as T
import random
import pprint

from Baralho import Carta

CORES_VALIDAS = ("amarelo", "azul", "verde", "vermelho")

class Jogador:
    def __init__(self, cartas: T.List[Carta]):
        self.cartas = cartas

    def selecionar(self, topo_descarte: Carta) -> T.List[Carta]:
        """
        Seleciona as cartas na mão que podem ser jogadas.
        :param topo_descarte: Topo da pilha de descarte.
            É garantido que exista um topo.
        :return: Lista de cartas selecionáveis
        """

        def filtro(topo: Carta, carta: Carta) -> bool:
            """
            Verifica se cor bate ou se o número bate.
            :param topo: Carta do topo do monte de descarte
            :param carta: Carta da mão para comparação
            :return: Cor é igual, tipo é igual ou é coringa
            """
            cor_bate = topo.cor == carta.cor
            tipo_bate = topo.tipo == carta.tipo
            eh_coringa = carta.cor == "preto"
            return cor_bate or tipo_bate or eh_coringa

        selecionadas = [carta for carta in self.cartas if filtro(topo_descarte, carta)]

        return selecionadas

    def comprar(self, quantidade: int, monte_compra: T.List[Carta]) -> T.List[Carta]:
        """
        Caso eu não consiga selecionar nenhuma carta,
        preciso comprar uma (ou mais).
        
        :param quantidade: Quantidade de cartas a comprar
        :param monte_compra: Monte de cartas de comprar
        """
        for _ in range(quantidade):                
            carta_comprada = monte_compra.pop()
            self.cartas.append(carta_comprada)
            
        return monte_compra
    
    @staticmethod
    def escolher_carta_possivel(cartas_possiveis: T.List[Carta]) -> T.Optional[Carta]:
        """
        Escolhe uma carta das várias cartas possíveis.
        Retorna None caso não tenham cartas, mas é esperado que se tenha.
        :param cartas_possiveis: Lista de cartas possíveis
        :return: Carta selecionada (ou None)
        """
        if not cartas_possiveis:
            return None

        idx_carta = None
        while idx_carta is None:
            idx_carta_str = input(
                f"Selecione a carta [0, {len(cartas_possiveis) - 1}]: "
            )

            eh_decimal = idx_carta_str.isdecimal()
            eh_valor_valido = idx_carta_str and 0 <= int(idx_carta_str) < len(
                cartas_possiveis
            )
            if eh_decimal and eh_valor_valido:
                return cartas_possiveis[int(idx_carta_str)]

            print(f"Dê um número de 0 a {len(cartas_possiveis) - 1}")

    def jogar(self, carta: Carta, monte_descarte: T.List[Carta]) -> T.List[Carta]:
        """
        Tira uma carta da mão e coloca no monte de descarte.
        :param carta: Carta selecionada
        :param monte_descarte: Monte de descarte
        """
        self.cartas.remove(carta)
        monte_descarte.insert(0, carta)
        return monte_descarte
    
    @staticmethod
    def escolher_cor_de_coringa() -> str:
        """
        Escolhe uma das 4 cores de coringa.
        :return: Cor escolhida
        """
        cor_escolhida = None
        while cor_escolhida not in CORES_VALIDAS:
            cor_escolhida = input("Escolha uma cor (amarelo, azul, verde, vermelho): ").lower()
            if cor_escolhida not in CORES_VALIDAS:
                print(
                    "Cor inválida.\n" f'Escolha uma entre {", ".join(CORES_VALIDAS)}.'
                )
        return cor_escolhida
    
    def __str__(self):
        return "Cartas: " + ", ".join(str(carta) for carta in self.cartas)

