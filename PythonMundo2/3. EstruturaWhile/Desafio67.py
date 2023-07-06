while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado.")
        break
    
    print("Tabuada de", numero, ":")
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)