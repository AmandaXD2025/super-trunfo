import time
import os
from src.baralho import Baralho
from src.jogador import Jogador

class Jogo:
    """Gerencia a lógica principal e o fluxo do jogo Super Trunfo."""
    def __init__(self, nomes_jogadores=["Você", "Computador"]):
        self.baralho = Baralho()
        self.jogadores = [Jogador(nome) for nome in nomes_jogadores]
        self.distribuir_cartas()
        self.cartas_empate = []

    def distribuir_cartas(self):
        maos = self.baralho.distribuir(len(self.jogadores))
        for i, mao in enumerate(maos):
            self.jogadores[i].receber_cartas(mao)

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_status_rodada(self):
        print("="*30)
        print(f"🏆 PLACAR: {self.jogadores[0].nome} [{self.jogadores[0].numero_de_cartas}] vs [{self.jogadores[1].numero_de_cartas}] {self.jogadores[1].nome}")
        if self.cartas_empate:
            print(f"Cartas acumuladas no empate: {len(self.cartas_empate)}")
        print("="*30 + "\n")

    def jogar_rodada(self):
        self.limpar_tela()
        self.mostrar_status_rodada()

        jogador_atual = self.jogadores[0]
        oponente = self.jogadores[1]
        
        input("Pressione Enter para ver sua próxima carta...")
        print(f"Sua vez, {jogador_atual.nome}!\n")

        carta_jogador = jogador_atual.mostrar_carta_topo()
        print("Sua carta é:")
        print(carta_jogador)
        print("-" * 20)

        # Lógica do Super Trunfo
        if carta_jogador.super_trunfo:
            print("🎉🎉 VOCÊ TEM O SUPER TRUNFO! 🎉🎉")
            print("Você vence a rodada automaticamente!")
            vencedor = jogador_atual
            atributo_escolhido = "N/A (Super Trunfo)"
        else:
             # Escolha de atributo
            while True:
                escolha = input("Escolha um atributo (ataque, defesa, magia, velocidade): ").lower()
                if escolha in carta_jogador.atributos:
                    atributo_escolhido = escolha
                    break
                else:
                    print("Atributo inválido. Tente novamente.")

        carta_oponente = oponente.mostrar_carta_topo()

        print("\nO computador joga a carta:")
        print(carta_oponente)
        time.sleep(2)

        if carta_oponente.super_trunfo and not carta_jogador.super_trunfo:
            print("\n😢 O COMPUTADOR TEM O SUPER TRUNFO! 😢")
            print("O computador vence a rodada automaticamente!")
            vencedor = oponente
        elif not carta_jogador.super_trunfo:
            valor_jogador = carta_jogador.atributos[atributo_escolhido]
            valor_oponente = carta_oponente.atributos[atributo_escolhido]

            print(f"\n--- COMPARANDO {atributo_escolhido.upper()} ---")
            print(f"{jogador_atual.nome}: {valor_jogador} vs {oponente.nome}: {valor_oponente}")
            
            if valor_jogador > valor_oponente:
                vencedor = jogador_atual
                print(f"\n🎉 Você venceu a rodada! 🎉")
            elif valor_oponente > valor_jogador:
                vencedor = oponente
                print(f"\n😢 {oponente.nome} venceu a rodada. 😢")
            else:
                vencedor = None
                print("\n⚖️ EMPATE! As cartas serão acumuladas para a próxima rodada. ⚖️")

        # Gerencia as cartas
        cartas_na_mesa = [jogador_atual.jogar_carta(), oponente.jogar_carta()]
        self.cartas_empate.extend(cartas_na_mesa)

        if vencedor:
            vencedor.adicionar_cartas_ganhas(self.cartas_empate)
            print(f"{vencedor.nome} ganhou {len(self.cartas_empate)} carta(s)!")
            self.cartas_empate = [] # Limpa as cartas acumuladas
        
        time.sleep(4)


    def iniciar(self):
        """Inicia e executa o loop principal do jogo."""
        self.limpar_tela()
        print("--- BEM-VINDO AO SUPER TRUNFO DA FACULDADE ---")
        time.sleep(2)

        while all(p.numero_de_cartas > 0 for p in self.jogadores):
            self.jogar_rodada()
        
        self.limpar_tela()
        print("="*30)
        print("FIM DE JOGO!")
        for p in self.jogadores:
            if p.numero_de_cartas > 0:
                print(f"\n🏆 O GRANDE VENCEDOR É: {p.nome.upper()} 🏆")
        print("="*30)

if __name__ == '__main__':
    jogo = Jogo()
    jogo.iniciar()