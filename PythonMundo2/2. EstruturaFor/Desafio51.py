# Programa para calcular os 10 primeiros termos de uma Progressão Aritmética

# Lendo o primeiro termo e a razão
primeiro_termo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))

# Calculando e imprimindo os 10 primeiros termos
for i in range(1, 11):
    termo = primeiro_termo + (i-1) * razao
    print(f'{i}º termo: {termo}')
