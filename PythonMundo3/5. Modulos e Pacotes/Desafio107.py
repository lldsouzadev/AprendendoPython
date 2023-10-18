# main.py
from utilidadesCeV import moeda

valor = float(input('Digite o valor: '))
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'Aumentando 10% temos {moeda.aumentar(valor, 10)}')
print(f'Diminuindo 10% temos {moeda.diminuir(valor, 10)}')
