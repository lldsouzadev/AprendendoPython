primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro_termo
contador = 1
total_termos = 0

while contador <= 10:
    print(termo_atual, end=" ")
    termo_atual += razao
    contador += 1
    total_termos += 1

print()  # Imprime uma quebra de linha no final

while True:
    quantidade_termos = int(input("Digite o número de termos adicionais que deseja exibir (0 para sair): "))

    if quantidade_termos == 0:
        print("Programa encerrado.")
        break

    contador = 1

    while contador <= quantidade_termos:
        termo_atual += razao
        print(termo_atual, end=" ")
        contador += 1
        total_termos += 1

    print()  # Imprime uma quebra de linha no final

print("Total de termos exibidos:", total_termos)