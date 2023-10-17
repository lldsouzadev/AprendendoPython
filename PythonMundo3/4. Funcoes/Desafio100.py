import random

# Lista de números
numeros = []

# Função para sortear 5 números e adicionar na lista
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
    print('PRONTO!')

# Função para somar os números pares da lista
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

# Executa as funções
sorteia(numeros)
somaPar(numeros)
