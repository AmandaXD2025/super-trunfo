import pandas as pd
import random
from src.carta import Carta

class Baralho:
    """Gerencia o carregamento e a distribuição das cartas."""
    def __init__(self, caminho_arquivo='data/cartas.csv'):
        self.cartas = self._carregar_cartas(caminho_arquivo)
        self.embaralhar()

    def _carregar_cartas(self, caminho_arquivo):
        """Carrega as cartas a partir de um arquivo CSV."""
        df = pd.read_csv(caminho_arquivo)
        return [Carta(**linha) for linha in df.to_dict(orient='records')]

    def embaralhar(self):
        """Embaralha as cartas do baralho."""
        random.shuffle(self.cartas)

    def distribuir(self, num_jogadores):
        """Distribui as cartas o mais igualmente possível entre os jogadores."""
        maos = [[] for _ in range(num_jogadores)]
        for i, carta in enumerate(self.cartas):
            maos[i % num_jogadores].append(carta)
        return maos