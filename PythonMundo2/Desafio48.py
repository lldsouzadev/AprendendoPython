# Inicializa a variável de soma
soma = 0

# Itera através do intervalo de 1 a 500
for num in range(1, 501):

    # Verifica se o número é múltiplo de três
    if num % 3 == 0:
        # Adiciona o número à soma
        soma += num

# Imprime a soma
print(soma)
