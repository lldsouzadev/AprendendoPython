def voto(ano_nascimento):
    """
    Função para determinar a elegibilidade para votar com base no ano de nascimento.
    
    Parâmetros:
    ano_nascimento (int): O ano de nascimento da pessoa.

    Retorna:
    str: Uma string indicando se o voto é 'NEGADO', 'OPCIONAL' ou 'OBRIGATÓRIO'.
    """
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

# Solicita ao usuário que insira o ano de nascimento
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
print(voto(ano_nascimento))
