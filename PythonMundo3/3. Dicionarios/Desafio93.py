# Inicializando o dicionário
jogador = {}

# Lendo o nome do jogador e a quantidade de partidas
jogador['nome'] = input("Digite o nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Lendo a quantidade de gols em cada partida
jogador['gols'] = []
for i in range(partidas):
    jogador['gols'].append(int(input(f"Quantos gols na partida {i+1}? ")))

# Calculando o total de gols
jogador['total'] = sum(jogador['gols'])

print(jogador)
