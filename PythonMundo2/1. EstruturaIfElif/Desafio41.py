ano_nascimento = int(input("Informe o ano de nascimento do atleta: "))
idade = 2022 - ano_nascimento

if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Junior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"

print("A categoria do atleta é:", categoria)
