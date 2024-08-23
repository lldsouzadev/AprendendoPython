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

def jogar():
    """
    Função principal para executar o jogo da velha.
    
    Retorna:
        None
    """
    tabuleiro = [' ' for _ in range(9)]
    jogador_atual = 'X'
    
    print("Bem-vindo ao Jogo da Velha!")
    
    while True:
        exibir_tabuleiro(tabuleiro)
        try:
            movimento = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[movimento] != ' ':
                print("Essa posição já está ocupada. Escolha outra.")
                continue
            tabuleiro[movimento] = jogador_atual
            
            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns! O jogador {jogador_atual} venceu!")
                break
            
            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break
            
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        
        except (ValueError, IndexError):
            print("Escolha inválida! Por favor, escolha um número entre 1 e 9 que corresponda a uma posição vazia no tabuleiro.")
    
    print("Fim do jogo.")

if __name__ == "__main__":
    jogar()
