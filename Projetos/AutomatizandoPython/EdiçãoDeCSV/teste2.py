import pandas as pd
import xlsxwriter
import os

# Dados de exemplo
data = {
    'Mês': ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'],
    'Receitas': [82549, 79867, 71786, 66469, 63948, 74715, 75218, 97822, 74187, 67932, 67565, 58761],
    'Despesas': [65305, 33210, 29953, 37068, 39148, 27932, 46782, 56771, 44951, 44614, 17948, 41290],
}
df = pd.DataFrame(data)

# Definir o caminho do arquivo
script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, "dashboard_financeiro_avancado.xlsx")

# Criar um arquivo Excel
workbook = xlsxwriter.Workbook(excel_path)
worksheet = workbook.add_worksheet('Dashboard')

# Formatos
title_format = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center', 'valign': 'vcenter'})
header_format = workbook.add_format({'bold': True, 'bg_color': '#4472C4', 'font_color': 'white', 'align': 'center'})
number_format = workbook.add_format({'num_format': '#,##0', 'align': 'right'})

# Título
worksheet.merge_range('A1:G1', 'Dashboard Financeiro', title_format)

# Cabeçalhos
headers = ['Mês', 'Receitas', 'Despesas', 'Resultado']
for col, header in enumerate(headers):
    worksheet.write(2, col, header, header_format)

# Dados
for row, (_, data_row) in enumerate(df.iterrows(), start=3):
    worksheet.write(row, 0, data_row['Mês'])
    worksheet.write(row, 1, data_row['Receitas'], number_format)
    worksheet.write(row, 2, data_row['Despesas'], number_format)
    worksheet.write(row, 3, f'=B{row+1}-C{row+1}', number_format)

# Gráfico
chart = workbook.add_chart({'type': 'column'})
chart.add_series({
    'name': 'Receitas',
    'categories': f'=Dashboard!$A$4:$A${3+len(df)}',
    'values': f'=Dashboard!$B$4:$B${3+len(df)}',
})
chart.add_series({
    'name': 'Despesas',
    'categories': f'=Dashboard!$A$4:$A${3+len(df)}',
    'values': f'=Dashboard!$C$4:$C${3+len(df)}',
})
chart.set_title({'name': 'Receitas vs Despesas'})
chart.set_x_axis({'name': 'Mês'})
chart.set_y_axis({'name': 'Valor'})
worksheet.insert_chart('I3', chart)

# Totais
worksheet.write('A16', 'Total', header_format)
worksheet.write('B16', f'=SUM(B4:B15)', number_format)
worksheet.write('C16', f'=SUM(C4:C15)', number_format)
worksheet.write('D16', f'=B16-C16', number_format)

workbook.close()

print(f"Arquivo Excel criado em: {excel_path}")
