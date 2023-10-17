def area(largura, comprimento):
    return largura * comprimento

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

print(f"A área do terreno é {area(largura, comprimento)} metros quadrados.")
