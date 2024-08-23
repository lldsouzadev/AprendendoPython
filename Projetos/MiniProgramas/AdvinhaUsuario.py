import os

def limpar_tela():
    """
    Limpa a tela do terminal.
    Funciona tanto em Windows quanto em sistemas Unix-like.
    """
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas Unix-like (Linux, macOS)
        os.system('clear')

def jogo_adivinhacao():
    """
    Jogo de adivinhação entre dois usuários.
    O Usuário 1 escolhe um número entre 1 e 25, e o Usuário 2 tenta adivinhar.
    Para cada tentativa, o programa informa se o número é maior, menor ou se o Usuário 2 acertou.
    
    Retorna:
        None
    """
    
    print("Usuário 1, escolha um número entre 1 e 25.")
    
    # Captura o número escolhido pelo Usuário 1
    while True:
        try:
            numero_secreto = int(input("Digite o número para o Usuário 2 adivinhar: "))
            
            if numero_secreto < 1 or numero_secreto > 25:
                print("Por favor, escolha um número entre 1 e 25.")
            else:
                break
        
        except ValueError:
            print("Por favor, digite um número válido.")
    
    limpar_tela()  # Limpa a tela antes do Usuário 2 adivinhar
    
    print("Usuário 2, agora é sua vez de adivinhar o número!")
    tentativas = 0
    acertou = False
    
    while not acertou:
        try:
            palpite = int(input("Digite o seu palpite: "))
            tentativas += 1
            
            if palpite < 1 or palpite > 25:
                print("Por favor, digite um número entre 1 e 25.")
                continue
            
            if palpite < numero_secreto:
                print("O número é maior que", palpite)
            elif palpite > numero_secreto:
                print("O número é menor que", palpite)
            else:
                print(f"Parabéns, Usuário 2! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                acertou = True
        
        except ValueError:
            print("Por favor, digite um número válido.")
    
    print("Fim do jogo.")

if __name__ == "__main__":
    jogo_adivinhacao()
