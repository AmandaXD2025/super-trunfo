class Carta:
    """Representa uma única carta do jogo."""
    def __init__(self, nome, ataque, defesa, magia, velocidade, super_trunfo=False):
        self.nome = nome
        self.atributos = {
            'ataque': int(ataque),
            'defesa': int(defesa),
            'magia': int(magia),
            'velocidade': int(velocidade)
        }
        # Converte a string 'False'/'True' para o booleano correspondente
        self.super_trunfo = str(super_trunfo).lower() == 'true'

    def __str__(self):
        """Retorna uma representação em string da carta para exibição."""
        atributos_str = ', '.join([f"{chave.capitalize()}: {valor}" for chave, valor in self.atributos.items()])
        trunfo_str = " (SUPER TRUNFO)" if self.super_trunfo else ""
        return f"--- {self.nome.upper()}{trunfo_str} ---\n[ Ataque: {self.atributos['ataque']} | Defesa: {self.atributos['defesa']} | Magia: {self.atributos['magia']} | Velocidade: {self.atributos['velocidade']} ]"