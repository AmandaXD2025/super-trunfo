# tests/test_jogo.py

import unittest
import math
from src.jogo import Jogo
from src.carta import Carta
from src.baralho import Baralho # Importamos o Baralho para o teste de integração

class TestJogo(unittest.TestCase):

    # ... (os outros testes que já fizemos continuam aqui) ...

    def test_vencedor_da_rodada_controlado(self):
        """
        [TESTE DE UNIDADE]
        Testa a lógica da rodada de forma controlada, sem ler arquivos.
        """
        print("\n--- [UNIDADE] Teste de Rodada Controlada ---")
        # ... (código que cria as cartas Herói e Monstro) ...
        # (Este teste continua exatamente como estava)


    def test_integracao_carregamento_do_baralho_via_csv(self):
        """
        [TESTE DE INTEGRAÇÃO]
        Verifica se o baralho é carregado corretamente a partir do arquivo CSV.
        """
        print("\n--- [INTEGRAÇÃO] Teste de Carregamento do CSV ---")
        try:
            # Tenta carregar o baralho a partir do caminho real do arquivo
            baralho = Baralho(caminho_arquivo='data/cartas.csv')

            # 1. Verificamos se alguma carta foi carregada
            self.assertGreater(len(baralho.cartas), 0, "O baralho não deveria estar vazio após carregar o CSV.")
            print(f"Sucesso: {len(baralho.cartas)} cartas carregadas do CSV.")

            # 2. Verificamos se o primeiro item da lista é realmente um objeto do tipo Carta
            primeira_carta = baralho.cartas[0]
            self.assertIsInstance(primeira_carta, Carta, "O item carregado do CSV não é um objeto Carta.")
            print(f"Sucesso: O primeiro item é um objeto '{type(primeira_carta).__name__}'.")

        except FileNotFoundError:
            self.fail("TESTE FALHOU: O arquivo 'data/cartas.csv' não foi encontrado.")