numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
    'dezoito', 'dezenove', 'vinte'
)

numero = int(input('Digite um número entre 0 e 20: '))

if 0 <= numero <= 20:
    extenso = numeros_por_extenso[numero]
    print(f'O número {numero} por extenso é: {extenso}.')
else:
    print('Número inválido. Por favor, digite um número entre 0 e 20.')