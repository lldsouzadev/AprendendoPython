import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Obter o diretório atual onde app.py está localizado
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para o dataset.csv
csv_path = os.path.join(base_dir, 'data', 'dataset.csv')

# Inicializar o aplicativo Dash com o tema Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Função para carregar os dados
def carregar_dados():
    return pd.read_csv(csv_path)

# Função para salvar os dados
def salvar_dados(df):
    df.to_csv(csv_path, index=False)

# Carregar os dados
df = carregar_dados()

# Supondo que seu dataset tenha as colunas 'Categoria', 'Data', 'Vendas', 'Quantidade', 'Preço_Unitario'
categorias = df['Categoria'].unique()

# Definir o layout do dashboard
app.layout = dbc.Container(
    [
        # Cabeçalho
        dbc.Row(
            dbc.Col(
                html.H1("Dashboard Interativo de Dados", className="text-center my-4"),
                width=12
            )
        ),

        # Seção de Filtros
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Selecione Categorias"),
                        dcc.Dropdown(
                            id='filtro-categoria',
                            options=[{'label': categoria, 'value': categoria} for categoria in categorias],
                            value=list(categorias),
                            multi=True,
                            placeholder="Selecione categorias"
                        )
                    ],
                    width=12
                )
            ],
            className="mb-4"
        ),

        # Seção de Gráficos
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='grafico-vendas'),
                    width=6
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(id='grafico-pizza')
                        ),
                        className="mb-4"
                    ),
                    width=6
                )
            ]
        ),

        # Seção de Gerenciamento de Dados
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Gerenciar Dados"),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Categoria"),
                                        dcc.Dropdown(
                                            id='input-categoria',
                                            options=[{'label': categoria, 'value': categoria} for categoria in categorias],
                                            placeholder="Selecione uma categoria"
                                        )
                                    ],
                                    width=6
                                ),
                                dbc.Col(
                                    [
                                        html.Label("Data"),
                                        dcc.DatePickerSingle(
                                            id='input-data',
                                            placeholder="Selecione uma data"
                                        )
                                    ],
                                    width=6
                                )
                            ]
                        ),
                        html.Label("Vendas"),
                        dcc.Input(id='input-vendas', type='number', placeholder="Insira o valor das vendas"),
                        html.Label("Quantidade"),
                        dcc.Input(id='input-quantidade', type='number', placeholder="Insira a quantidade"),
                        html.Div(
                            [
                                html.Button('Adicionar', id='btn-adicionar', n_clicks=0, className="mt-2"),
                                html.Button('Editar', id='btn-editar', n_clicks=0, className="mt-2 ml-2"),
                                html.Button('Excluir', id='btn-excluir', n_clicks=0, className="mt-2 ml-2")
                            ],
                            className="mt-3"
                        ),
                        html.Div(id='output-mensagem', className="mt-2")
                    ],
                    width=12
                )
            ],
            className="mb-4"
        ),

        # Tabela de Dados
        dbc.Row(
            dbc.Col(
                dash.dash_table.DataTable(
                    id='tabela-dados',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                    editable=True,
                    row_selectable='single',
                    selected_rows=[],
                    page_size=10,
                    style_header={
                        'backgroundColor': '#333333',
                        'color': '#e0e0e0'
                    },
                    style_cell={
                        'backgroundColor': '#222222',
                        'color': '#e0e0e0'
                    },
                    style_table={
                        'backgroundColor': '#333333'
                    }
                ),
                width=12
            )
        )
    ],
    fluid=True,
)

# Definir callbacks para atualizar os gráficos com base nos filtros
@app.callback(
    [Output('grafico-vendas', 'figure'),
     Output('grafico-pizza', 'figure')],
    [Input('filtro-categoria', 'value'),
     Input('tabela-dados', 'data')]
)
def atualizar_graficos(selecoes, rows):
    df = pd.DataFrame(rows)
    if not selecoes:
        # Se nenhuma categoria for selecionada, exibir todos
        filtrado = df
    else:
        # Filtrar o DataFrame com base nas categorias selecionadas
        filtrado = df[df['Categoria'].isin(selecoes)]
    
    # Criar o gráfico de barras
    fig_bar = px.bar(
        filtrado,
        x='Categoria',
        y='Vendas',
        title="Vendas por Categoria",
        labels={'Vendas': 'Total de Vendas', 'Categoria': 'Categoria do Produto'},
        template='plotly_dark'  # Alterar o template para 'plotly_dark'
    )
    
    # Atualizar o layout do gráfico de barras
    fig_bar.update_layout(
        xaxis_title="Categoria",
        yaxis_title="Total de Vendas",
        plot_bgcolor='#121212',
        paper_bgcolor='#121212',
        font=dict(color='#e0e0e0')
    )
    
    # Criar o gráfico de pizza em 3D
    fig_pizza = go.Figure(
        data=[go.Pie(
            labels=filtrado['Categoria'],
            values=filtrado['Vendas'],
            hole=0.3
        )]
    )
    
    # Atualizar o layout do gráfico de pizza
    fig_pizza.update_traces(
        hoverinfo='label+percent',
        textinfo='value',
        textfont_size=12,
        marker=dict(line=dict(color='#000000', width=2)),
        pull=[0.1 if v == max(filtrado['Vendas']) else 0 for v in filtrado['Vendas']]
    )
    fig_pizza.update_layout(
        title="Distribuição de Vendas por Categoria",
        template='plotly_dark',
        showlegend=True,
        plot_bgcolor='#121212',
        paper_bgcolor='#121212',
        font=dict(color='#e0e0e0')
    )
    
    return fig_bar, fig_pizza

# Callback para gerenciar dados
@app.callback(
    [Output('tabela-dados', 'data'),
     Output('output-mensagem', 'children'),
     Output('filtro-categoria', 'options')],
    [Input('btn-adicionar', 'n_clicks'),
     Input('btn-editar', 'n_clicks'),
     Input('btn-excluir', 'n_clicks')],
    [State('input-categoria', 'value'),
     State('input-data', 'date'),
     State('input-vendas', 'value'),
     State('input-quantidade', 'value'),
     State('tabela-dados', 'data'),
     State('tabela-dados', 'selected_rows')]
)
def gerenciar_dados(n_adicionar, n_editar, n_excluir, categoria, data, vendas, quantidade, rows, selected_rows):
    ctx = dash.callback_context
    if not ctx.triggered:
        return rows, "", [{'label': cat, 'value': cat} for cat in categorias]
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    df = pd.DataFrame(rows)

    if button_id == 'btn-adicionar':
        if categoria and data and vendas and quantidade:
            preco_unitario = vendas / quantidade if quantidade != 0 else 0
            novo_registro = pd.DataFrame([{'Categoria': categoria, 'Data': data, 'Vendas': vendas, 'Quantidade': quantidade, 'Preço_Unitario': preco_unitario}])
            df = pd.concat([df, novo_registro], ignore_index=True)
            salvar_dados(df)
            categorias_atualizadas = df['Categoria'].unique()
            return df.to_dict('records'), "Dados adicionados com sucesso!", [{'label': cat, 'value': cat} for cat in categorias_atualizadas]
        else:
            return rows, "Por favor, preencha todos os campos.", [{'label': cat, 'value': cat} for cat in categorias]

    if button_id == 'btn-editar' and selected_rows:
        if categoria and data and vendas and quantidade:
            preco_unitario = vendas / quantidade if quantidade != 0 else 0
            row_id = selected_rows[0]
            df.loc[row_id] = {'Categoria': categoria, 'Data': data, 'Vendas': vendas, 'Quantidade': quantidade, 'Preço_Unitario': preco_unitario}
            salvar_dados(df)
            categorias_atualizadas = df['Categoria'].unique()
            return df.to_dict('records'), "Dados editados com sucesso!", [{'label': cat, 'value': cat} for cat in categorias_atualizadas]
        else:
            return rows, "Por favor, preencha todos os campos.", [{'label': cat, 'value': cat} for cat in categorias]

    if button_id == 'btn-excluir' and selected_rows:
        row_id = selected_rows[0]
        df = df.drop(row_id).reset_index(drop=True)
        salvar_dados(df)
        categorias_atualizadas = df['Categoria'].unique()
        return df.to_dict('records'), "Dados excluídos com sucesso!", [{'label': cat, 'value': cat} for cat in categorias_atualizadas]

    return rows, "", [{'label': cat, 'value': cat} for cat in categorias]

# Executar o servidor
if __name__ == "__main__":
    app.run_server(debug=True)