a = int(input("Insira o lado 1: "))
b = int(input("Insira o lado 2: "))
c = int(input("Insira o lado 3: "))

if a == b and b == c:
    print("Triângulo Equilátero")
elif a == b or a == c or b == c:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")
