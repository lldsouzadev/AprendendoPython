valores = tuple(int(input(f"Digite o {i+1}º valor: ")) for i in range(4))

# A) Quantas vezes apareceu o valor 9
contagem_9 = valores.count(9)
print(f"O valor 9 apareceu {contagem_9} vez(es).")

# B) Em que posição foi digitado o primeiro valor 3
posicao_3 = valores.index(3) if 3 in valores else None
if posicao_3 is not None:
    print(f"O primeiro valor 3 foi digitado na posição {posicao_3 + 1}.")
else:
    print("O valor 3 não foi digitado.")

# C) Quais foram os números pares
numeros_pares = [valor for valor in valores if valor % 2 == 0]
print("Os números pares digitados foram:", ", ".join(map(str, numeros_pares)))
