def eh_palindromo(frase):
    # Remover os espaços em branco da frase
    frase_sem_espacos = frase.replace(" ", "")
    
    # Converter a frase para letras minúsculas
    frase_sem_espacos = frase_sem_espacos.lower()

    # Verificar se a frase invertida é igual à frase original usando um loop for
    for i in range(len(frase_sem_espacos)):
        if frase_sem_espacos[i] != frase_sem_espacos[-i-1]:
            return False
    
    return True

# Ler a frase do usuário
frase = input("Digite uma frase: ")

# Exibir a frase original
print("Frase original:", frase)

# Verificar se a frase é um palíndromo
if eh_palindromo(frase):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

# Exibir a frase resultante (sem espaços e em letras minúsculas)
frase_sem_espacos = frase.replace(" ", "")
frase_sem_espacos = frase_sem_espacos.lower()
print("Frase resultante:", frase_sem_espacos)