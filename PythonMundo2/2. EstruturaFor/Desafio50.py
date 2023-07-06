soma = 0
for i in range(6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma += num
print("Soma dos números pares:", soma)
