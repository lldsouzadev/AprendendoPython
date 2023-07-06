continuar = True
soma = 0
contador = 0
maior = float('-inf')
menor = float('inf')

while continuar:
    numero = int(input("Digite um número inteiro: "))
    
    soma += numero
    contador += 1
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero
    
    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() != "s":
        continuar = False

if contador > 0:
    media = soma / contador
    print("Média:", media)
    print("Maior valor:", maior)
    print("Menor valor:", menor)
else:
    print("Nenhum número foi digitado.")