def jogo_adivinhacao():
    palavra = input("Jogador 1, digite uma palavra: ")
    palavra = palavra.lower()
    tentativas = 6
    adivinhacoes = ['_' for _ in palavra]

    print("Jogador 2, você tem 6 tentativas para adivinhar a palavra.")
    print(' '.join(adivinhacoes))

    while tentativas > 0 and '_' in adivinhacoes:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    adivinhacoes[i] = letra
            print(' '.join(adivinhacoes))
        else:
            tentativas -= 1
            print(f"Letra incorreta. Você tem {tentativas} tentativas restantes.")

    if '_' not in adivinhacoes:
        print("Parabéns, você adivinhou a palavra!")
    else:
        print(f"Você perdeu. A palavra era '{palavra}'.")

jogo_adivinhacao()
