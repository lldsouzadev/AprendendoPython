import random

def adivinhar_numero():
    """
    Jogo de adivinhação de número entre 1 e 25.
    O computador escolhe um número aleatório e o usuário tenta adivinhar.
    Para cada tentativa, o programa informa se o número é maior, menor ou se o usuário acertou.
    
    Retorna:
        None
    """
    
    numero_secreto = random.randint(1, 25)
    tentativas = 0
    acertou = False
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 25.")

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
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                acertou = True
        
        except ValueError:
            print("Por favor, digite um número válido.")
    
    print("Fim do jogo.")

if __name__ == "__main__":
    adivinhar_numero()
