num = int(input("Insira um número: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "não é um número primo")
            break
    else:
        print(num, "é um número primo")
else:
    print(num, "não é um número primo")
