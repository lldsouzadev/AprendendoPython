# Inicializando as listas
numeros = [[], []]

for i in range(7):
    num = int(input("Digite um número: "))
    
    # Verificando se o número é par ou ímpar
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

# Ordenando as listas
numeros[0].sort()
numeros[1].sort()

# Imprimindo os resultados
print(f"Os números pares digitados foram: {numeros[0]}")
print(f"Os números ímpares digitados foram: {numeros[1]}")
