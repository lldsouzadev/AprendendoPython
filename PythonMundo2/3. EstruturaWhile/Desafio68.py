import random

def jogo_par_impar():
    vitorias_consecutivas = 0
    
    while True:
        jogador_escolha = input("Escolha par (P) ou ímpar (I): ").upper()
        jogador_numero = int(input("Digite um número entre 0 e 10: "))
        
        while jogador_numero < 0 or jogador_numero > 10:
            jogador_numero = int(input("Número inválido. Digite um número entre 0 e 10: "))
        
        computador_numero = random.randint(0, 10)
        total = jogador_numero + computador_numero
        
        print(f"Você escolheu {jogador_numero} e o computador escolheu {computador_numero}.")
        print(f"A soma é {total}.")
        
        if (total % 2 == 0 and jogador_escolha == "P") or (total % 2 != 0 and jogador_escolha == "I"):
            print("Você venceu!")
            vitorias_consecutivas += 1
        else:
            print("Você perdeu!")
            break
    
    print(f"\nTotal de vitórias consecutivas: {vitorias_consecutivas}")
    
jogo_par_impar()