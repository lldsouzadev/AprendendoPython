import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 10)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 0 e 10.")

    while True:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("O número secreto é maior! Tente novamente.")
        elif palpite > numero_secreto:
            print("O número secreto é menor! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")
            break

jogo_adivinhacao()