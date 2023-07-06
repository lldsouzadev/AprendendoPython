# Inicializando as variáveis do maior e menor peso com valores inválidos
maior_peso = float('-inf')
menor_peso = float('inf')

# Loop para ler o peso de cada pessoa
for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    
    # Atualizando o maior e menor peso, se necessário
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

# Mostrando o maior e menor peso lidos
print(f"O maior peso lido foi: {maior_peso}")
print(f"O menor peso lido foi: {menor_peso}")