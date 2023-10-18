def leiaDinheiro(mensagem):
    """
    Lê um valor monetário, aceitando apenas valores válidos.
    
    Parâmetros:
    mensagem (str): A mensagem a ser exibida ao solicitar a entrada do usuário.
    
    Retorna:
    float: O valor monetário inserido pelo usuário.
    """
    while True:
        valor = str(input(mensagem)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'ERRO: "{valor}" é um preço inválido!')
        else:
            return float(valor)
