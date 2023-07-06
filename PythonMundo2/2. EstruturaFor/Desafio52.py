num = int(input("Insira um número: "))

if num > 1:
    divisible = False
    print("Números que precedem o número escolhido: ")
    for i in range(2, num):
        if (num % i) == 0:
            print("\033[1;33m",i,"\033[0m")
            divisible = True
        else:
            print("\033[1;31m",i,"\033[0m")
    if divisible:
        print(num, "não é um número primo")
    else:
        print(num, "é um número primo")
else:
    print(num, "não é um número primo")