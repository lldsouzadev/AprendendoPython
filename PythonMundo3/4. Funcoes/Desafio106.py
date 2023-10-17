# Definindo algumas cores
class cores:
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AZUL = '\033[34m'
    CIANO = '\033[36m'
    MAGENTA = '\033[35m'
    AMARELO = '\033[33m'
    PRETO = '\033[30m'
    BRANCO = '\033[37m'
    RESETAR = '\033[0;0m'
    NEGRITO = '\033[1m'
    REVERSO = '\033[2m'
    FUNDO_VERMELHO = '\033[41m'
    FUNDO_VERDE = '\033[42m'
    FUNDO_AZUL = '\033[44m'

def manual_interativo(i):
    """
    Função para fornecer um manual interativo do Python.
    
    O usuário pode digitar qualquer comando Python válido e o manual para esse comando será exibido.
    
    Recebe um argumento:
        i (int): índice para selecionar a cor de fundo.
    
    Retorna: comando (str) inserido pelo usuário.
    """
    
    cores_fundo = [cores.FUNDO_VERMELHO, cores.FUNDO_VERDE, cores.FUNDO_AZUL]
    
    print(cores_fundo[i % len(cores_fundo)] + "Digite um comando Python para ver o manual ou 'FIM' para sair:" + cores.RESETAR)
    comando = input()
    
    return comando

i = 0
while True:
    comando = manual_interativo(i)
    
    if comando.upper() == 'FIM':
        break
    else:
        try:
            help(comando)
        except Exception as e:
            print(cores.VERMELHO + "Erro: " + str(e) + cores.RESETAR)
    
    i += 1
