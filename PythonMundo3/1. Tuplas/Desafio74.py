import random

numeros_aleatorios = tuple(random.sample(range(1, 101), 5))

print("Números gerados:")
for numero in numeros_aleatorios:
    print(numero)

menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)

print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)