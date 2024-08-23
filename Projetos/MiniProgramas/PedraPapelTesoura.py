import random

def escolha_computador():
    """
    Faz a escolha aleatória do computador entre Pedra, Papel e Tesoura.
    
    Retorna:
        str: A escolha do computador ('Pedra', 'Papel' ou 'Tesoura').
    """
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    return random.choice(escolhas)

def determinar_vencedor(escolha_usuario, escolha_computador):
    """
    Determina o vencedor com base nas escolhas do usuário e do computador.
    
    Parâmetros:
        escolha_usuario (str): A escolha do usuário ('Pedra', 'Papel' ou 'Tesoura').
        escolha_computador (str): A escolha do computador ('Pedra', 'Papel' ou 'Tesoura').
    
    Retorna:
        str: O resultado do jogo ('Vitória', 'Derrota' ou 'Empate').
    """
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == 'Pedra' and escolha_computador == 'Tesoura') or \
         (escolha_usuario == 'Papel' and escolha_computador == 'Pedra') or \
         (escolha_usuario == 'Tesoura' and escolha_computador == 'Papel'):
        return "Vitória"
    else:
        return "Derrota"

def jogar():
    """
    Função principal para executar o jogo de Pedra, Papel e Tesoura.
    
    Retorna:
        None
    """
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    print("Escolha: Pedra, Papel ou Tesoura")
    
    while True:
        escolha_usuario = input("Digite sua escolha: ").capitalize()
        
        if escolha_usuario not in ['Pedra', 'Papel', 'Tesoura']:
            print("Escolha inválida! Por favor, escolha entre Pedra, Papel ou Tesoura.")
            continue
        
        escolha_pc = escolha_computador()
        print(f"O computador escolheu: {escolha_pc}")
        
        resultado = determinar_vencedor(escolha_usuario, escolha_pc)
        if resultado == "Vitória":
            print("Parabéns! Você venceu!")
        elif resultado == "Derrota":
            print("Que pena! Você perdeu.")
        else:
            print("Foi um empate!")
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    jogar()
