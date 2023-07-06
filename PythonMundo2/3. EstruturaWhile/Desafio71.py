def caixa_eletronico(valor):
    cedulas = [50, 20, 10, 1]
    quantidade_cedulas = [0, 0, 0, 0]

    for i in range(len(cedulas)):
        if valor >= cedulas[i]:
            quantidade_cedulas[i] = valor // cedulas[i]
            valor = valor % cedulas[i]

    return quantidade_cedulas

# Pergunta ao usuário o valor a ser sacado
valor_saque = int(input("Digite o valor a ser sacado: "))

# Chama a função caixa_eletronico e exibe o resultado
resultado = caixa_eletronico(valor_saque)

print("Quantidade de cédulas:")
print(f"R$50: {resultado[0]}")
print(f"R$20: {resultado[1]}")
print(f"R$10: {resultado[2]}")
print(f"R$1: {resultado[3]}")