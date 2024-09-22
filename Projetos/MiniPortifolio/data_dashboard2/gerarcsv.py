# generate_csv.py
import pandas as pd
import numpy as np

# Dados fictícios para simulação
data = {
    "Data": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "Receita": np.random.randint(500, 2000, 30),
    "Despesa": np.random.randint(300, 1500, 30),
    "Subarea": np.random.choice(["Marketing", "Vendas", "Operações"], 30)
}

df = pd.DataFrame(data)
df.to_csv('fluxo_caixa.csv', index=False)
