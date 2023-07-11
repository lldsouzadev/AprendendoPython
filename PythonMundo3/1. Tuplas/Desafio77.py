palavras = ("python", "programacao", "linguagem", "computador", "desenvolvimento")

vogais = ("a", "e", "i", "o", "u")

for palavra in palavras:
    vogais_palavra = []
    for letra in palavra:
        if letra.lower() in vogais:
            vogais_palavra.append(letra)
    print(f"Vogais da palavra '{palavra}': {', '.join(vogais_palavra)}")
