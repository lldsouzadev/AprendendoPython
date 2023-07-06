while True:
    print("===== MENU =====")
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Sair do programa")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print("A soma é:", soma)
    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        multiplicacao = num1 * num2
        print("A multiplicação é:", multiplicacao)
    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num1 > num2:
            print("O maior número é:", num1)
        elif num2 > num1:
            print("O maior número é:", num2)
        else:
            print("Os números são iguais.")
    elif opcao == 4:
        continue
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Digite um número entre 1 e 5.")
    
    print("\n")