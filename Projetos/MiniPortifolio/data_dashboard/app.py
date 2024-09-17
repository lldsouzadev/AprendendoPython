import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Inicializar o aplicativo Dash com o tema Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Carregar os dados
# Certifique-se de que o arquivo 'dataset.csv' está na pasta 'data/'
df = pd.read_csv('data/dataset.csv')

# Verificar as primeiras linhas do DataFrame (opcional)
# print(df.head())

# Supondo que seu dataset tenha as colunas 'Categoria' e 'Vendas'
# Ajuste os nomes das colunas conforme necessário
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
                    width=4
                )
            ],
            className="mb-4"
        ),

        # Seção de Gráficos
        dbc.Row(
            dbc.Col(
                dcc.Graph(id='grafico-vendas'),
                width=12
            )
        ),
    ],
    fluid=True,
)

# Definir callbacks para atualizar os gráficos com base nos filtros
@app.callback(
    Output('grafico-vendas', 'figure'),
    [Input('filtro-categoria', 'value')]
)
def atualizar_grafico(selecoes):
    if not selecoes:
        # Se nenhuma categoria for selecionada, exibir todos
        filtrado = df
    else:
        # Filtrar o DataFrame com base nas categorias selecionadas
        filtrado = df[df['Categoria'].isin(selecoes)]
    
    # Criar o gráfico de barras
    fig = px.bar(
        filtrado,
        x='Categoria',
        y='Vendas',
        title="Vendas por Categoria",
        labels={'Vendas': 'Total de Vendas', 'Categoria': 'Categoria do Produto'},
        template='plotly_dark'  # Você pode alterar o template conforme preferência
    )
    
    # Atualizar o layout do gráfico
    fig.update_layout(
        xaxis_title="Categoria",
        yaxis_title="Total de Vendas",
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        font=dict(color='#333')
    )
    
    return fig

# Executar o servidor
if __name__ == "__main__":
    app.run_server(debug=True)