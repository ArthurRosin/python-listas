# Questão 1

import pandas as pd

df_mercado_um = pd.read_csv("fake-mercado12.csv")
df_mercado_dois = pd.read_csv("fake-mercado09.csv")
df_mercado_tres = pd.read_csv("fake-mercado01.csv")

mercado_geral = []
mercado_um = []
mercado_dois = []
mercado_tres = []

#categoria, it, Menor Valor, Mercado = [], [], [], [], []

for itens in range(8):
    item = str(input())
    mercado_u = df_mercado_um.query(f'Item == "{item}"').values.tolist()
    for dados_um in mercado_u:
        mercado_um.append(dados_um)
    mercado_d = df_mercado_dois.query(f'Item == "{item}"').values.tolist()
    for dados_dois in mercado_d:
        mercado_dois.append(dados_dois)  
    mercado_t = df_mercado_tres.query(f'Item == "{item}"').values.tolist()
    for dados_tres in mercado_t:
        mercado_tres.append(dados_tres)

mercado_geral.append(mercado_um)
mercado_geral.append(mercado_dois)
mercado_geral.append(mercado_tres)

for dados in mercado_geral:
    for classe in dados:
        

