classificacao_2017 = (
    'Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
    'Botafogo', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG',
    'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Vitória',
    'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO', 'Atlético-PR'
)

# a) Os 5 primeiros times
print("Os 5 primeiros times:")
for i in range(5):
    print(classificacao_2017[i])
print()

# b) Os últimos 4 colocados
print("Os últimos 4 colocados:")
for i in range(-4, 0):
    print(classificacao_2017[i])
print()

# c) Times em ordem alfabética
print("Times em ordem alfabética:")
classificacao_2017_ordenada = sorted(classificacao_2017)
for time in classificacao_2017_ordenada:
    print(time)
print()

# d) Posição do Fluminense
fluminense_posicao = classificacao_2017.index('Fluminense')
print(f"O Fluminense está na posição: {fluminense_posicao + 1}")