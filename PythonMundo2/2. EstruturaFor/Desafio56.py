# Lista para armazenar os dados das pessoas
pessoas = []

# Loop para ler os dados das 4 pessoas
for i in range(4):
    print(f"Digite os dados da pessoa {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ")

    # Adiciona os dados da pessoa à lista
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

# Calcula a média de idade do grupo
soma_idades = sum(pessoa["idade"] for pessoa in pessoas)
media_idades = soma_idades / len(pessoas)

# Encontra o homem mais velho
homens = [pessoa for pessoa in pessoas if pessoa["sexo"].upper() == "M"]
homem_mais_velho = max(homens, key=lambda x: x["idade"])["nome"]

# Conta quantas mulheres têm menos de 20 anos
mulheres_jovens = len([pessoa for pessoa in pessoas if pessoa["sexo"].upper() == "F" and pessoa["idade"] < 20])

# Imprime os resultados
print(f"Média de idade do grupo: {media_idades:.2f}")
print(f"Nome do homem mais velho: {homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_jovens}")