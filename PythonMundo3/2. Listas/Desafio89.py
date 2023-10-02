# Inicializando a lista de alunos
alunos = []

while True:
    # Lendo o nome e as notas do aluno
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    
    # Calculando a média do aluno
    media = (nota1 + nota2) / 2
    
    # Adicionando o aluno à lista de alunos
    alunos.append([nome, [nota1, nota2], media])
    
    # Perguntando ao usuário se ele quer continuar
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in 'Nn':
        break

# Imprimindo o boletim
print("BOLETIM")
for i, aluno in enumerate(alunos):
    print(f"{i} - {aluno[0]} tem média {aluno[2]}")

# Permitindo que o usuário veja as notas de cada aluno individualmente
while True:
    escolha = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if escolha == 999:
        break
    if escolha <= len(alunos) - 1:
        print(f"As notas de {alunos[escolha][0]} são {alunos[escolha][1]}")
