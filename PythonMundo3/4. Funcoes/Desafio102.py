def fatorial(n, show=False):
    """
    Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

# Solicita ao usuário que insira os parâmetros
num = int(input("Digite um número para calcular o fatorial: "))
mostrar_calculo = input("Deseja ver o cálculo? (s/n) ").lower() == 's'
print(fatorial(num, mostrar_calculo))
