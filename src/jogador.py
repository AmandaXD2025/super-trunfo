class Jogador:
    """Representa um jogador no jogo com sua mão de cartas."""
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    @property
    def numero_de_cartas(self):
        """Retorna o número de cartas na mão do jogador."""
        return len(self.mao)

    def receber_cartas(self, cartas):
        """Adiciona uma lista de cartas à mão do jogador."""
        self.mao.extend(cartas)

    def mostrar_carta_topo(self):
        """Retorna a carta no topo da mão sem removê-la."""
        return self.mao[0] if self.mao else None

    def jogar_carta(self):
        """Remove e retorna a carta do topo da mão."""
        return self.mao.pop(0)

    def adicionar_cartas_ganhas(self, cartas_ganhas):
        """Adiciona as cartas ganhas no fundo da mão."""
        self.mao.extend(cartas_ganhas)