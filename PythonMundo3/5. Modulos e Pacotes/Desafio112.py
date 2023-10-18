# main.py
from utilidadesCeV import moeda, dados

valor = dados.leiaDinheiro('Digite o valor: R$')
formatar = input('Deseja formatar o resultado como moeda? (s/n) ') == 's'
moeda.resumo(valor, 10, formatar)
