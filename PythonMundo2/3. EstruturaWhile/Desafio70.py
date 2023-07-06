total_gasto = 0
produtos_mais_de_mil = 0
produto_mais_barato = None
preco_mais_barato = 0

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$"))

    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_mais_de_mil += 1

    if produto_mais_barato is None or preco_produto < preco_mais_barato:
        produto_mais_barato = nome_produto
        preco_mais_barato = preco_produto

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() != 'S':
        break

print("=== Resultado ===")
print("Total gasto na compra: R$", total_gasto)
print("Quantidade de produtos que custam mais de R$1000:", produtos_mais_de_mil)
print("Nome do produto mais barato:", produto_mais_barato)