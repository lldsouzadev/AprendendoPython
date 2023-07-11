produtos_precos = (
    ("Camiseta", 29.99),
    ("Calça Jeans", 59.99),
    ("Tênis", 99.99),
    ("Meias", 9.99),
    ("Jaqueta", 79.99)
)

print("Listagem de Preços")
print("------------------")
print("Produto\t\tPreço")
print("------------------")

for produto, preco in produtos_precos:
    print(f"{produto.ljust(15)}R${preco:.2f}")

print("------------------")