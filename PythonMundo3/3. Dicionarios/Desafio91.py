import random
from operator import itemgetter

# Inicializando o dicionário
jogadores = {}

# Jogando o dado para cada jogador
for i in range(1, 5):
    jogadores[f'jogador{i}'] = random.randint(1, 6)

print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado.")

# Ordenando o dicionário pelo valor (número tirado no dado)
jogadores_ordenados = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))

print("\nRanking dos jogadores:")
for i, v in enumerate(jogadores_ordenados.items()):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}.")
