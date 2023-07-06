peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = "Abaixo do Peso"
elif imc >= 18.5 and imc < 25:
    status = "Peso ideal"
elif imc >= 25 and imc < 30:
    status = "Sobrepeso"
elif imc >= 30 and imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade Morbida"

print("Seu IMC é:", imc)
print("Você está na faixa de: ", status)
