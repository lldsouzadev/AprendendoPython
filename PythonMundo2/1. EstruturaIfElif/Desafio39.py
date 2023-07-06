import datetime

# Solicita o ano de nascimento do jovem
ano_nascimento = int(input("Informe o ano de nascimento: "))

# Obtém a idade do jovem
hoje = datetime.datetime.now()
idade = hoje.year - ano_nascimento

# Verifica se o jovem já passou do tempo de se alistar
if idade > 18:
    print("Você já passou do tempo de se alistar. Seu atraso é de", idade - 18, "ano(s).")

# Verifica se é a hora do jovem se alistar
elif idade == 18:
    print("É hora de se alistar.")

# Caso contrário, o jovem ainda vai se alistar
else:
    print("Ainda falta", 18 - idade, "ano(s) para você se alistar.")
