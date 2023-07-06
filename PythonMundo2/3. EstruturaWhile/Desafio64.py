numeros = []
soma = 0

while True:
    numero = int(input("Digite um número inteiro (999 para parar): "))
    
    if numero == 999:
        break
    
    numeros.append(numero)
    soma += numero

quantidade_numeros = len(numeros)

print(f"Foram digitados {quantidade_numeros} números.")
print(f"A soma dos números digitados é: {soma}.")