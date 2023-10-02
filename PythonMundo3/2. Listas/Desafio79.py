# Inicializando a lista
numeros = []

while True:
    num = int(input("Digite um número: "))
    
    # Verificando se o número já existe na lista
    if num not in numeros:
        numeros.append(num)
        print("Número adicionado com sucesso!")
    else:
        print("Número duplicado! Não vou adicionar...")
    
    # Perguntando ao usuário se ele quer continuar
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in 'Nn':
        break

# Ordenando a lista
numeros.sort()

# Imprimindo os resultados
print(f"Os números digitados foram: {numeros}")
