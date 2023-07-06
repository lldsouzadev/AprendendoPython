num = int(input("Digite um número inteiro: "))

print("Escolha uma das opções abaixo para a conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input())

if opcao == 1:
    print(bin(num))
elif opcao == 2:
    print(oct(num))
elif opcao == 3:
    print(hex(num))
else:
    print("Opção inválida.")
