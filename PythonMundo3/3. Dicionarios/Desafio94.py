pessoas = []
soma_idades = 0

while True:
    pessoa = {}
    pessoa['nome'] = input("Digite o nome: ")
    while True:
        pessoa['sexo'] = input("Digite o sexo (M/F): ").upper()
        if pessoa['sexo'] in 'MF':
            break
        print("Erro! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Digite a idade: "))
    soma_idades += pessoa['idade']
    pessoas.append(pessoa)
    while True:
        resp = input("Quer continuar? (S/N) ").upper()
        if resp in 'SN':
            break
        print("Erro! Responda apenas S ou N.")
    if resp == 'N':
        break

print(f"\nA) Ao todo temos {len(pessoas)} pessoas cadastradas.")
media = soma_idades / len(pessoas)
print(f"B) A média de idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram ", end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f"{p['nome']} ", end='')
print()
print("D) Lista das pessoas que estão acima da média: ")
for p in pessoas:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< ENCERRADO >>")
