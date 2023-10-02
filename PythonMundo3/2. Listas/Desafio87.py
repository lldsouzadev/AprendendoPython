# Inicializando a matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Variáveis para armazenar as somas e o maior valor
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

# Preenchendo a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))
        
        # Verificando se o valor é par
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        
        # Somando os valores da terceira coluna
        if j == 2:
            soma_terceira_coluna += matriz[i][j]
        
        # Encontrando o maior valor da segunda linha
        if i == 1 and matriz[i][j] > maior_segunda_linha:
            maior_segunda_linha = matriz[i][j]

# Imprimindo a matriz
print("A matriz é:")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()

# Imprimindo os resultados
print(f"A soma de todos os valores pares digitados é: {soma_pares}")
print(f"A soma dos valores da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {maior_segunda_linha}")
