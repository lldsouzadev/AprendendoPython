# main.py
from utilidadesCeV import moeda

valor = float(input('Digite o valor: '))
formatar = input('Deseja formatar o resultado como moeda? (s/n) ') == 's'
print(f'O dobro de {valor} é {moeda.dobro(valor, formatar)}')
print(f'A metade de {valor} é {moeda.metade(valor, formatar)}')
print(f'Aumentando 10% temos {moeda.aumentar(valor, 10, formatar)}')
print(f'Diminuindo 10% temos {moeda.diminuir(valor, 10, formatar)}')
