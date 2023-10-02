# Inicializando a lista
pessoas = []

while True:
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa: "))
    pessoas.append((nome, peso))
    
    # Perguntando ao usuário se ele quer continuar
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in 'Nn':
        break

# Encontrando as pessoas mais pesadas e mais leves
mais_pesadas = [nome for nome, peso in pessoas if peso == max(pessoas, key=lambda item:item[1])[1]]
mais_leves = [nome for nome, peso in pessoas if peso == min(pessoas, key=lambda item:item[1])[1]]

# Imprimindo os resultados
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"As pessoas mais pesadas são: {mais_pesadas}")
print(f"As pessoas mais leves são: {mais_leves}")
