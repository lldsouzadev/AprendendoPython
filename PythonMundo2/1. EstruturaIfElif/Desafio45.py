import random

print("Jogo de Jokenpô!")

# Lista de opções de jogada
jogadas = ["Pedra", "Papel", "Tesoura"]

# Loop do jogo
while True:
    # Pedir jogada do usuário
    jogada_usuario = input("Escolha sua jogada (Pedra, Papel, Tesoura): ")

    # Verificar se a jogada do usuário é válida
    if jogada_usuario not in jogadas:
        print("Jogada inválida.")
        continue

    # Escolher jogada do computador
    jogada_computador = random.choice(jogadas)

    # Exibir jogadas
    print("Jogada do usuário: " + jogada_usuario)
    print("Jogada do computador: " + jogada_computador)

    # Verificar resultado
    if jogada_usuario == jogada_computador:
        print("Empate.")
    elif (jogada_usuario == "Pedra" and jogada_computador == "Tesoura") or (jogada_usuario == "Papel" and jogada_computador == "Pedra") or (jogada_usuario == "Tesoura" and jogada_computador == "Papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu.")

    # Perguntar se o usuário quer jogar novamente
    novo_jogo = input("Deseja jogar novamente? (s/n) ")
    if novo_jogo != "s":
        break
