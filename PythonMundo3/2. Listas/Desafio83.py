# Solicitando ao usuário que digite uma expressão
expressao = input("Digite uma expressão: ")

# Inicializando uma pilha para os parênteses
pilha = []

# Analisando a expressão
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

# Verificando se a expressão é válida
if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")
