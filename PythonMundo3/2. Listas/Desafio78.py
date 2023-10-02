# Inicializando a lista
numeros = []

# Lendo os 5 valores
for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

# Encontrando o maior e o menor valor e suas posições
maior = max(numeros)
menor = min(numeros)
pos_maior = [i for i, x in enumerate(numeros) if x == maior]
pos_menor = [i for i, x in enumerate(numeros) if x == menor]

# Imprimindo os resultados
print(f"O maior valor digitado foi {maior} nas posições {pos_maior}")
print(f"O menor valor digitado foi {menor} nas posições {pos_menor}")
