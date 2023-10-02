# Inicializando a lista
numeros = []

while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    
    # Perguntando ao usuário se ele quer continuar
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in 'Nn':
        break

# Ordenando a lista de forma decrescente
numeros.sort(reverse=True)

# Verificando se o valor 5 está na lista
valor_5 = "está na lista" if 5 in numeros else "não está na lista"

# Imprimindo os resultados
print(f"Você digitou {len(numeros)} números.")
print(f"A lista de valores, ordenada de forma decrescente, é: {numeros}")
print(f"O valor 5 {valor_5}.")
