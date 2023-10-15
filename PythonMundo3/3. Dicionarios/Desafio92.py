from datetime import datetime

# Inicializando o dicionário
pessoa = {}

# Lendo os dados da pessoa
pessoa['nome'] = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
pessoa['idade'] = datetime.now().year - ano_nascimento
pessoa['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))

# Se a pessoa tem carteira de trabalho, ler os dados adicionais
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input("Ano de contratação: "))
    pessoa['salario'] = float(input("Salário: R$"))
    pessoa['aposentadoria'] = ((pessoa['contratacao'] + 35) - datetime.now().year) + pessoa['idade']

print(pessoa)
