# Super Trunfo - Desafio de Faculdade

Este é um projeto de um jogo de cartas "Super Trunfo" desenvolvido em Python como um desafio para a disciplina de Programação. O jogo é executado no terminal e utiliza um arquivo `.csv` para gerenciar as cartas.

## 🃏 Regras do Jogo

O objetivo do Super Trunfo é ganhar todas as cartas do seu oponente.

1.  As cartas são distribuídas igualmente entre os dois jogadores.
2.  A cada rodada, o jogador da vez escolhe um atributo da sua carta do topo.
3.  O jogador com o maior valor no atributo escolhido vence a rodada e fica com a carta do oponente.
4.  Se uma carta for um "Super Trunfo", ela vence qualquer outra carta, a menos que o oponente também tenha uma (neste caso, as regras normais se aplicam).
5.  Em caso de empate, cada jogador recebe sua carta de volta.
6.  O jogo termina quando um dos jogadores fica sem cartas.

## ⚙️ Estrutura do Projeto

```
super-trunfo/
├── data/
│   └── cartas.csv
├── src/
│   ├── jogo.py
│   └── ...
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

-   **`data/`**: Contém o arquivo `cartas.csv` com os dados das cartas.
-   **`src/`**: Contém todo o código fonte do jogo, dividido em classes para melhor organização.
-   **`README.md`**: Esta documentação.
-   **`requirements.txt`**: Lista de dependências Python.

## 🚀 Como Executar

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute o jogo:**
    ```bash
    python src/jogo.py
    ```

## 🛠️ Tecnologias Utilizadas

-   **Python 3**
-   **Pandas** (para leitura do arquivo CSV)