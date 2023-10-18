import cadastro

while True:
    try:
        cadastro.mostrar_menu()
        
        opcao = int(input("\nSua Opção: "))
        
        if opcao == 1:
            cadastro.ver_pessoas_cadastradas()
        elif opcao == 2:
            cadastro.cadastrar_nova_pessoa()
        elif opcao == 3:
            cadastro.sair_do_sistema()
        else:
            raise ValueError("ERRO: Digite uma opção válida.")
    except ValueError:
        print("ERRO: por favor, digite um número inteiro válido.")
