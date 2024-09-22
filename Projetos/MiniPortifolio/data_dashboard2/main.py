import fasthtml
import pandas as pd

# Função para carregar e salvar dados
CSV_PATH = "fluxo_caixa.csv"

def load_data():
    return pd.read_csv(CSV_PATH)

def save_data(df):
    df.to_csv(CSV_PATH, index=False)

# Iniciando o app FastHTML
app = FastHTML("Dashboard de Fluxo de Caixa")

# Carregando dados do CSV
df = load_data()

# Renderizando tabela
def render_table():
    rows = [list(row) for _, row in df.iterrows()]
    table = Table(headers=["Data", "Receita", "Despesa", "Subarea", "Ações"], rows=rows)

    for idx, _ in df.iterrows():
        table.add_action(Button("Editar", lambda idx=idx: edit_entry(idx)))
        table.add_action(Button("Deletar", lambda idx=idx: delete_entry(idx)))

    return table

# Funções de edição, adição e remoção
def add_entry(data, receita, despesa, subarea):
    df.loc[len(df)] = [data, int(receita), int(despesa), subarea]
    save_data(df)
    app.refresh()

def edit_entry(index):
    entry = df.iloc[index]
    app.show_modal(
        "Editar Entrada",
        inputs=[
            Input("Data", value=entry["Data"]),
            Input("Receita", value=str(entry["Receita"])),
            Input("Despesa", value=str(entry["Despesa"])),
            Input("Subarea", value=entry["Subarea"])
        ],
        buttons=[Button("Salvar", lambda: save_entry(index))]
    )

def save_entry(index):
    df.iloc[index] = [app.get_value("Data"), app.get_value("Receita"), app.get_value("Despesa"), app.get_value("Subarea")]
    save_data(df)
    app.close_modal()
    app.refresh()

def delete_entry(index):
    df.drop(index, inplace=True)
    save_data(df)
    app.refresh()

# Adicionando funcionalidades e renderizando componentes
app.add_component(render_table())
app.add_component(
    [
        Text("Adicionar Nova Entrada"),
        Input("Data", placeholder="YYYY-MM-DD"),
        Input("Receita", placeholder="Receita"),
        Input("Despesa", placeholder="Despesa"),
        Input("Subarea", placeholder="Subarea"),
        Button("Adicionar", lambda: add_entry(app.get_value("Data"), app.get_value("Receita"), app.get_value("Despesa"), app.get_value("Subarea")))
    ]
)

# Rodando a aplicação
app.run()
