from datetime import date

ano_atual = date.today().year
maiores_idade = 0
menores_idade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print(f"\nMaiores de idade: {maiores_idade}")
print(f"Menores de idade: {menores_idade}")