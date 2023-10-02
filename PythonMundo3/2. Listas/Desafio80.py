# Inicializando a lista
numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    
    # Verificando onde o número deve ser inserido
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        for j in range(len(numeros)):
            if num <= numeros[j]:
                numeros.insert(j, num)
                break

# Imprimindo os resultados
print(f"Os números digitados foram: {numeros}")
