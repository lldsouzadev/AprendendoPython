primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

contador = 1
termo_atual = primeiro_termo

while contador <= 10:
    print(termo_atual, end=" ")
    termo_atual += razao
    contador += 1

print()  # Imprime uma quebra de linha no final