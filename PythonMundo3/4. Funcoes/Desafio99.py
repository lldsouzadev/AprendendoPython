def maior(*numeros):
    return max(numeros)

# Solicita ao usuário para inserir uma lista de números
numeros = list(map(int, input("Digite os números separados por espaço: ").split()))

print(f'O maior número é: {maior(*numeros)}')
