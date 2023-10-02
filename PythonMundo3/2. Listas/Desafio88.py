import random

# Perguntando ao usuário quantos jogos serão gerados
num_jogos = int(input("Quantos jogos serão gerados? "))

# Inicializando a lista de jogos
jogos = []

for i in range(num_jogos):
    # Gerando um jogo
    jogo = sorted(random.sample(range(1, 61), 6))
    
    # Adicionando o jogo à lista de jogos
    jogos.append(jogo)

# Imprimindo os jogos
for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")
