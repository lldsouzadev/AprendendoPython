import random

def exibir_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro do jogo da velha.
    
    Parâmetros:
        tabuleiro (list): Uma lista de 9 elementos representando o estado atual do tabuleiro.
    
    Retorna:
        None
    """
    print("\n")
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    print("\n")

def verificar_vencedor(tabuleiro, jogador):
    """
    Verifica se o jogador atual venceu o jogo.
    
    Parâmetros:
        tabuleiro (list): Uma lista de 9 elementos representando o estado atual do tabuleiro.
        jogador (str): O símbolo do jogador ('X' ou 'O').
    
    Retorna:
        bool: True se o jogador venceu, False caso contrário.
    """
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]  # Diagonais
    ]
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    """
    Verifica se o jogo terminou em empate.
    
    Parâmetros:
        tabuleiro (list): Uma lista de 9 elementos representando o estado atual do tabuleiro.
    
    Retorna:
        bool: True se o jogo terminou em empate, False caso contrário.
    """
    return all(spot in ['X', 'O'] for spot in tabuleiro)

def movimento_ia(tabuleiro):
    """
    Realiza o movimento da IA usando uma estratégia básica.
    
    Parâmetros:
        tabuleiro (list): Uma lista de 9 elementos representando o estado atual do tabuleiro.
    
    Retorna:
        int: A posição escolhida pela IA (0-8).
    """
    # 1. Verifica se a IA pode ganhar no próximo movimento
    for i in range(9):
        copia_tabuleiro = tabuleiro[:]
        if copia_tabuleiro[i] == ' ':
            copia_tabuleiro[i] = 'O'
            if verificar_vencedor(copia_tabuleiro, 'O'):
                return i

    # 2. Verifica se o jogador pode ganhar no próximo movimento e bloqueia
    for i in range(9):
        copia_tabuleiro = tabuleiro[:]
        if copia_tabuleiro[i] == ' ':
            copia_tabuleiro[i] = 'X'
            if verificar_vencedor(copia_tabuleiro, 'X'):
                return i

    # 3. Tenta pegar uma das posições centrais
    if tabuleiro[4] == ' ':
        return 4

    # 4. Tenta pegar uma das posições nos cantos
    movimentos = [0, 2, 6, 8]
    movimentos_validos = [m for m in movimentos if tabuleiro[m] == ' ']
    if movimentos_validos:
        return random.choice(movimentos_validos)

    # 5. Tenta pegar as laterais
    movimentos = [1, 3, 5, 7]
    movimentos_validos = [m for m in movimentos if tabuleiro[m] == ' ']
    if movimentos_validos:
        return random.choice(movimentos_validos)

    # 6. Se nenhum movimento foi possível, retorna -1
    return -1

def jogar():
    """
    Função principal para executar o jogo da velha contra a IA.
    
    Retorna:
        None
    """
    tabuleiro = [' ' for _ in range(9)]
    jogador_humano = 'X'
    jogador_ia = 'O'
    
    print("Bem-vindo ao Jogo da Velha!")
    print("Você é o 'X' e jogará contra a IA 'O'.")

    while True:
        exibir_tabuleiro(tabuleiro)

        # Movimento do Jogador Humano
        while True:
            try:
                movimento = int(input(f"Escolha uma posição (1-9): ")) - 1
                if tabuleiro[movimento] == ' ':
                    tabuleiro[movimento] = jogador_humano
                    break
                else:
                    print("Essa posição já está ocupada. Escolha outra.")
            except (ValueError, IndexError):
                print("Escolha inválida! Por favor, escolha um número entre 1 e 9 que corresponda a uma posição vazia no tabuleiro.")
        
        # Verifica se o jogador humano venceu
        if verificar_vencedor(tabuleiro, jogador_humano):
            exibir_tabuleiro(tabuleiro)
            print("Parabéns! Você venceu!")
            break

        # Verifica se o jogo terminou em empate
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        # Movimento da IA
        movimento = movimento_ia(tabuleiro)
        if movimento != -1:
            tabuleiro[movimento] = jogador_ia

        # Verifica se a IA venceu
        if verificar_vencedor(tabuleiro, jogador_ia):
            exibir_tabuleiro(tabuleiro)
            print("Que pena! A IA venceu!")
            break

        # Verifica se o jogo terminou em empate
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

    print("Fim do jogo.")

if __name__ == "__main__":
    jogar()
