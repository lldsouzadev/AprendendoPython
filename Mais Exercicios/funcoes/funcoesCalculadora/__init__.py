def adicao(x, y):
   """
   Esta função recebe dois números, x e y, e retorna a soma de x e y.
   """
   return x + y

def subtracao(x, y):
   """
   Esta função recebe dois números, x e y, e retorna a diferença de x e y.
   """
   return x - y

def multiplicacao(x, y):
   """
   Esta função recebe dois números, x e y, e retorna o produto de x e y.
   """
   return x * y

def divisao(x, y):
   """
   Esta função recebe dois números, x e y. Retorna o quociente de x e y se y não for zero.
   Caso contrário, retorna uma mensagem de erro.
   """
   if y != 0:
       return x / y
   else:
       return 'Divisão por zero não é permitida'

def potencia(x, y):
    """
    Esta função recebe dois números, x e y, e retorna o valor de x elevado à potência de y.
    """
    return x ** y

def raiz_quadrada(x):
    """
    Esta função recebe um número x e retorna a raiz quadrada de x se x for maior ou igual a zero.
    Caso contrário, retorna uma mensagem de erro.
    """
    if x >= 0:
        return x ** 0.5
    else:
        return 'Não é possível calcular a raiz quadrada de um número negativo'

def exibir_menu():
    """
    Esta função exibe o menu da calculadora e retorna a escolha do usuário.
    """
    print('\033[1;34;40m' + '-'*30)
    print('Menu:')
    print('\t1. Adição')
    print('\t2. Subtração')
    print('\t3. Multiplicação')
    print('\t4. Divisão')
    print('\t5. Potência')
    print('\t6. Raiz Quadrada')
    print('\t7. Sair')
    print('-'*30 + '\033[0m')
    
    escolha = input('\033[1;32;40m' + 'Escolha uma opção (1-7): ' + '\033[0m')
    
    return escolha