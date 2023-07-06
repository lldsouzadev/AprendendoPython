def calcular_fatorial(numero):
    fatorial = 1
    if numero < 0:
        return "O fatorial não pode ser calculado para números negativos."
    elif numero == 0:
        return "O fatorial de 0 é 1."
    else:
        for i in range(1, numero + 1):
            fatorial *= i
        return f"O fatorial de {numero} é {fatorial}."


numero = int(input("Digite um número inteiro: "))
resultado = calcular_fatorial(numero)
print(resultado)