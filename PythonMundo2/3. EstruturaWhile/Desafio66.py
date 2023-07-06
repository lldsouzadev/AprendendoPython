soma = contador = 0

while True:
    numero = int(input("Digite um número inteiro (999 para parar): "))

    if numero == 999:
        break

    soma += numero
    contador += 1

print(f"\nForam digitados {contador} números.")
print(f"A soma dos números digitados é: {soma}")