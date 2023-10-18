# main.py
from utilidadesCeV import moeda

valor = float(input('Digite o valor: '))
formatar = input('Deseja formatar o resultado como moeda? (s/n) ') == 's'
moeda.resumo(valor, 10, formatar)