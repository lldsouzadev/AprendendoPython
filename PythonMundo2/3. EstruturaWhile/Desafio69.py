# Inicializando as variáveis de contagem
maiores_dezoito = 0
homens_cadastrados = 0
mulheres_menos_vinte = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()

    # Verificando se a pessoa tem mais de 18 anos
    if idade > 18:
        maiores_dezoito += 1

    # Verificando se a pessoa é do sexo masculino
    if sexo == "M":
        homens_cadastrados += 1

    # Verificando se a pessoa é do sexo feminino e tem menos de 20 anos
    if sexo == "F" and idade < 20:
        mulheres_menos_vinte += 1

    opcao = input("Deseja continuar cadastrando pessoas? (S/N): ").upper()
    if opcao != "S":
        break

# Exibindo os resultados
print("Resultados:")
print("A) Pessoas com mais de 18 anos:", maiores_dezoito)
print("B) Homens cadastrados:", homens_cadastrados)