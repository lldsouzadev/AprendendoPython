def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
        print()
    else:
        for i in range(inicio, fim-1, -passo):
            print(i, end=' ')
        print()

# Contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)

# Contagem de 10 até 0, de 2 em 2
contador(10, 0, 2)

# Contagem personalizada
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
