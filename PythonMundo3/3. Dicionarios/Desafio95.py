def gerenciar_jogadores():
    jogadores = {}

    while True:
        nome = input("Digite o nome do jogador: ")
        partidas = int(input(f"Quantas partidas {nome} jogou? "))
        gols = []

        for i in range(partidas):
            gols.append(int(input(f"Quantos gols {nome} fez na partida {i+1}? ")))

        jogadores[nome] = {'partidas': partidas, 'gols': gols, 'total': sum(gols)}

        continuar = input("Deseja adicionar outro jogador? (S/N) ")
        if continuar.lower() != 's':
            break

    while True:
        nome = input("Digite o nome do jogador para ver detalhes: ")
        if nome in jogadores:
            print(f"Jogador: {nome}")
            print(f"Partidas Jogadas: {jogadores[nome]['partidas']}")
            print(f"Gols por partida: {jogadores[nome]['gols']}")
            print(f"Total de gols: {jogadores[nome]['total']}")
        else:
            print("Jogador não encontrado.")

        continuar = input("Deseja ver detalhes de outro jogador? (S/N) ")
        if continuar.lower() != 's':
            break

gerenciar_jogadores()
