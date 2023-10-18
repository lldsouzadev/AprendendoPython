def leiaInt(msg):
    """
    Função para ler um número inteiro.

    Parâmetros:
    msg (str): A mensagem a ser exibida para o usuário.

    Retorna:
    int: O número inteiro fornecido pelo usuário.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    """
    Função para ler um número flutuante.

    Parâmetros:
    msg (str): A mensagem a ser exibida para o usuário.

    Retorna:
    float: O número flutuante fornecido pelo usuário.
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número flutuante válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0.0
        else:
            return n

# Chamada das funções
n_int = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número inteiro {n_int}')

n_float = leiaFloat('Digite um número flutuante: ')
print(f'Você acabou de digitar o número flutuante {n_float}')
