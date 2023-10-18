# moeda.py
def aumentar(valor, porcentagem, formatar=False):
    """
    Aumenta o valor em uma certa porcentagem.
    
    Parâmetros:
    valor (float): O valor original.
    porcentagem (float): A porcentagem para aumentar o valor.
    formatar (bool): Se True, formata o resultado como moeda real (R$).
    
    Retorna:
    float ou str: O valor aumentado. Se formatar for True, retorna o valor formatado como moeda real (R$).
    """
    res = valor + (valor * porcentagem / 100)
    return moeda(res) if formatar else res

def diminuir(valor, porcentagem, formatar=False):
    """
    Diminui o valor em uma certa porcentagem.
    
    Parâmetros:
    valor (float): O valor original.
    porcentagem (float): A porcentagem para diminuir o valor.
    formatar (bool): Se True, formata o resultado como moeda real (R$).
    
    Retorna:
    float ou str: O valor diminuído. Se formatar for True, retorna o valor formatado como moeda real (R$).
    """
    res = valor - (valor * porcentagem / 100)
    return moeda(res) if formatar else res

def dobro(valor, formatar=False):
    """
    Calcula o dobro de um valor.
    
    Parâmetros:
    valor (float): O valor original.
    formatar (bool): Se True, formata o resultado como moeda real (R$).
    
    Retorna:
    float ou str: O dobro do valor. Se formatar for True, retorna o valor formatado como moeda real (R$).
    """
    res = valor * 2
    return moeda(res) if formatar else res

def metade(valor, formatar=False):
    """
    Calcula a metade de um valor.
    
    Parâmetros:
    valor (float): O valor original.
    formatar (bool): Se True, formata o resultado como moeda real (R$).
    
    Retorna:
    float ou str: A metade do valor. Se formatar for True, retorna o valor formatado como moeda real (R$).
    """
    res = valor / 2
    return moeda(res) if formatar else res

def moeda(valor):
   """
   Formata um valor como moeda real (R$).
   
   Parâmetros:
   valor (float): O valor a ser formatado.
   
   Retorna:
   str: O valor formatado como moeda real (R$).
   """
   return f'R$ {valor:.2f}'.replace('.', ',')

def resumo(valor, porcentagem, formatar=True):
    """
    Exibe um resumo das informações geradas pelas outras funções.
    
    Parâmetros:
    valor (float): O valor original.
    porcentagem (float): A porcentagem para aumentar e diminuir o valor.
    formatar (bool): Se True, formata os resultados como moeda real (R$).
    
    Retorna:
    None
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Dobro do valor: \t{dobro(valor, formatar)}')
    print(f'Metade do valor: \t{metade(valor, formatar)}')
    print(f'{porcentagem}% de aumento: \t{aumentar(valor, porcentagem, formatar)}')
    print(f'{porcentagem}% de redução: \t{diminuir(valor, porcentagem, formatar)}')
    print('-'*30)