# Inicializando o dicionário
aluno = {}

# Lendo o nome e a média do aluno
aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input("Digite a média do aluno: "))

# Determinando a situação do aluno
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

# Mostrando o conteúdo do dicionário
print(f"O aluno {aluno['nome']} foi {aluno['situacao']} com uma média de {aluno['media']}.")
