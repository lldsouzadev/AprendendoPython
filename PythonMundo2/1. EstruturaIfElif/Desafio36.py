# programa para aprovar empréstimo bancário para compra de casa

valor_casa = float(input("Qual é o valor da casa: "))
salario = float(input("Qual é o seu salário: "))
anos = int(input("Em quantos anos você pretende pagar o empréstimo: "))

# calculando o valor da prestação mensal
prestacao_mensal = valor_casa / (anos * 12)

# verificando se a prestação mensal não excede 30% do salário
if prestacao_mensal > (salario * 0.3):
    print("Empréstimo negado. A prestação mensal excede 30% do seu salário.")
else:
    print("Empréstimo aprovado. Valor da prestação mensal: ", prestacao_mensal)
