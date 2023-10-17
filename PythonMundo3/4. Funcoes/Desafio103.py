def ficha(nome='', gols=0):
    """
    Função que mostra a ficha de um jogador.
    
    Parâmetros:
    nome (str): O nome do jogador. O valor padrão é ''.
    gols (int): O número de gols que o jogador marcou. O valor padrão é 0.
    
    Retorna:
    str: Uma string que representa a ficha do jogador.
    """
    if nome.strip() == '':
        nome = '<desconhecido>'
    try:
        gols = int(gols)
    except ValueError:
        print("Erro! Você não digitou um número válido para o número de gols.")
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

# Solicitando ao usuário para inserir os parâmetros
nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')

# Chamando a função com os parâmetros fornecidos pelo usuário
print(ficha(nome, gols))
