def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)

texto = input("Digite o texto: ")
escreva(texto)
