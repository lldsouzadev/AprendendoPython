import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt
from io import BytesIO
import os

# Dados de exemplo
data = {
    'Dia': list(range(1, 32)),
    'Receitas': [20000, 0, 23000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Despesas': [5000, 0, 5800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
df = pd.DataFrame(data)
df['Saldo'] = df['Receitas'].cumsum() - df['Despesas'].cumsum()

# Definir o caminho do arquivo
script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, "dashboard_fluxo_caixa.xlsx")

# Criar um arquivo Excel
workbook = xlsxwriter.Workbook(excel_path)
worksheet = workbook.add_worksheet('Dashboard')

# Formatos
title_format = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#4F81BD', 'font_color': 'white'})
header_format = workbook.add_format({'bold': True, 'bg_color': '#4F81BD', 'font_color': 'white', 'align': 'center'})
number_format = workbook.add_format({'num_format': '#,##0', 'align': 'right'})
currency_format = workbook.add_format({'num_format': 'R$ #,##0.00', 'align': 'right'})

# Título
worksheet.merge_range('A1:H1', 'FLUXO DE CAIXA', title_format)

# Cabeçalhos
headers = ['Dia', 'Receitas', 'Despesas', 'Saldo']
for col, header in enumerate(headers):
    worksheet.write(2, col, header, header_format)

# Dados
for row, (_, data_row) in enumerate(df.iterrows(), start=3):
    worksheet.write(row, 0, data_row['Dia'])
    worksheet.write(row, 1, data_row['Receitas'], currency_format)
    worksheet.write(row, 2, data_row['Despesas'], currency_format)
    worksheet.write(row, 3, data_row['Saldo'], currency_format)

# Gráfico de Receitas, Despesas e Saldo
plt.figure(figsize=(10, 5))
plt.plot(df['Dia'], df['Receitas'], marker='o', label='Receitas', color='blue')
plt.plot(df['Dia'], df['Despesas'], marker='o', label='Despesas', color='red')
plt.plot(df['Dia'], df['Saldo'], marker='o', label='Saldo', color='purple')
plt.title('Receitas, Despesas e Saldo')
plt.xlabel('Dia')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)

# Salvar gráfico como imagem
img_buffer = BytesIO()
plt.savefig(img_buffer, format='png', dpi=300)
img_buffer.seek(0)

# Adicionar gráfico ao Excel
worksheet.insert_image('A5', 'image1', {'image_data': img_buffer, 'x_scale': 0.5, 'y_scale': 0.5})

# Gráfico de Maiores Despesas
despesas_data = {
    'Categoria': ['Encargos', 'Ordenado', 'Insumos', 'Impostos', 'Aluguel', 'Comissões', 'Rescisões'],
    'Valor': [27000, 24320, 14680, 13510, 12160, 4050, 4030]
}
df_despesas = pd.DataFrame(despesas_data)

plt.figure(figsize=(6, 4))
plt.barh(df_despesas['Categoria'], df_despesas['Valor'], color='brown')
plt.title('Maiores Despesas')
plt.xlabel('Valor')
plt.ylabel('Categoria')
plt.grid(True)

# Salvar gráfico como imagem
img_buffer = BytesIO()
plt.savefig(img_buffer, format='png', dpi=300)
img_buffer.seek(0)

# Adicionar gráfico ao Excel
worksheet.insert_image('A20', 'image2', {'image_data': img_buffer, 'x_scale': 0.5, 'y_scale': 0.5})

# Gráfico de Pizza Receitas vs Despesas
plt.figure(figsize=(4, 4))
plt.pie([df['Receitas'].sum(), df['Despesas'].sum()], labels=['Receitas', 'Despesas'], autopct='%1.1f%%', colors=['blue', 'red'])
plt.title('Receitas vs Despesas')

# Salvar gráfico como imagem
img_buffer = BytesIO()
plt.savefig(img_buffer, format='png', dpi=300)
img_buffer.seek(0)

# Adicionar gráfico ao Excel
worksheet.insert_image('E20', 'image3', {'image_data': img_buffer, 'x_scale': 0.5, 'y_scale': 0.5})

# Fechar workbook
workbook.close()

print(f"Arquivo Excel criado em: {excel_path}")