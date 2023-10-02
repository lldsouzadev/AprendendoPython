# Inicializando as listas
numeros = []
pares = []
impares = []

while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    
    # Verificando se o número é par ou ímpar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
    # Perguntando ao usuário se ele quer continuar
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in 'Nn':
        break

# Imprimindo os resultados
print(f"Os números digitados foram: {numeros}")
print(f"Os números pares digitados foram: {pares}")
print(f"Os números ímpares digitados foram: {impares}")
