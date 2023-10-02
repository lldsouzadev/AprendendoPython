# Inicializando a matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))

# Imprimindo a matriz
print("A matriz é:")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()