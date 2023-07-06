while True:
    sexo = input("Digite o sexo (M/F): ")
    if sexo.upper() == 'M' or sexo.upper() == 'F':
        break  # Valor correto, sai do loop
    else:
        print("Valor incorreto. Digite novamente.")

print("Sexo:", sexo.upper())