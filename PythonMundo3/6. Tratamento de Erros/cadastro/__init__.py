import os

# Lista de pessoas cadastradas
pessoas = []

def verificar_arquivo_existe(nome_arquivo):
    """
    Função para verificar se um arquivo existe.
    Retorna True se o arquivo existir, False caso contrário.
    """
    return os.path.exists(nome_arquivo)

def criar_arquivo(nome_arquivo):
    """
    Função para criar um arquivo .txt.
    Cria um arquivo com o nome especificado se ele não existir.
    """
    if not verificar_arquivo_existe(nome_arquivo):
        with open(nome_arquivo, 'w'):
            pass

def ler_arquivo(nome_arquivo):
    """
    Função para ler um arquivo .txt.
    Retorna uma lista de linhas no arquivo.
    """
    with open(nome_arquivo, 'r') as f:
        return f.readlines()


def cadastrar_nova_pessoa():
    """
    Função para cadastrar nova pessoa.
    Solicita ao usuário que digite o nome, a idade e o sexo da nova pessoa.
    Adiciona a nova pessoa a um arquivo .txt.
    """
    print("\n\033[44m\033[1m------------------ CADASTRO DE PESSOA ------------------\033[0m")
    
    print("\033[32mDigite o nome da nova pessoa:\033[0m")
    nome = input()
    
    print("\033[32mDigite a idade da nova pessoa:\033[0m")
    idade = input()
    
    print("\033[32mDigite o sexo da nova pessoa (M/F):\033[0m")
    sexo = input()
    
    nome_arquivo = 'pessoas.txt'
    
    try:
        criar_arquivo(nome_arquivo)
        
        with open(nome_arquivo, 'a') as f:
            f.write(f"{nome},{idade},{sexo}\n")
        
        print(f"\033[33m{nome}\033[0m \033[32mfoi cadastrado com sucesso!\033[0m")
    except Exception as e:
        print("\033[31mOcorreu um erro ao tentar cadastrar a nova pessoa:\033[0m", e)

def ver_pessoas_cadastradas():
    """
    Função para ver pessoas cadastradas.
    Lê o arquivo .txt e imprime o nome, a idade e o sexo de cada pessoa cadastrada em formato de tabela.
    """
    nome_arquivo = 'pessoas.txt'
    
    try:
        if verificar_arquivo_existe(nome_arquivo):
            linhas = ler_arquivo(nome_arquivo)
            
            if not linhas:
                print("\033[31mNenhuma pessoa cadastrada.\033[0m")
            else:
                print("{:<20} {:<10} {:<10}".format("Nome", "Idade", "Sexo"))
                print("-" * 40)
                
                for linha in linhas:
                    nome, idade, sexo = linha.strip().split(',')
                    print("{:<20} {:<10} {:<10}".format(nome, idade, sexo))
                    
        else:
            print("\033[31mNenhuma pessoa cadastrada.\033[0m")
    except Exception as e:
        print("\033[31mOcorreu um erro ao tentar exibir as pessoas cadastradas:\033[0m", e)


def sair_do_sistema():
    """
    Função para sair do sistema.
    Imprime uma mensagem informando que o sistema está sendo encerrado e encerra o programa.
    """
    print("Sair do sistema...")
    exit()

def mostrar_menu():
    """
    Função para mostrar o menu principal.
    Imprime o menu principal com opções para ver pessoas cadastradas, cadastrar nova pessoa e sair do sistema.
    """
    # Obtem a largura do terminal
    largura_terminal = os.get_terminal_size().columns

    # Imprime o menu com cor de fundo na linha inteira
    print("\n\033[34m{:<{}}\033[0m".format("------------------ MENU PRINCIPAL ------------------".ljust(largura_terminal), largura_terminal))
    print("\033[34m{:<{}}\033[0m".format("1 - Ver pessoas cadastradas".ljust(largura_terminal), largura_terminal))
    print("\033[34m{:<{}}\033[0m".format("2 - Cadastrar nova Pessoa".ljust(largura_terminal), largura_terminal))
    print("\033[34m{:<{}}\033[0m".format("3 - Sair do sistema".ljust(largura_terminal), largura_terminal))