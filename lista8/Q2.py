# Questão 2

import pandas as pd

df_mercado_um = pd.read_csv("fake-mercado01.csv")

lista = []
categoria, it, valor, quantidade, subtotal = [], [], [], [], []
for itens in range(7):
    produtos = str(input())
    dados_mercado = df_mercado_um.query(f'Item == "{produtos}"').values.tolist()
    lista.append(dados_mercado)

for dados in lista:
    for item in dados:
        if item[3] <= 2:
            categoria.append(item[0])
            it.append(item[1])
            valor.append(item[2])
            quantidade.append(item[3])
            subtotal.append((item[2] * item[3]))
        else:
            categoria.append(item[0])
            it.append(item[1])
            valor.append(item[2])
            quantidade.append(2)
            subtotal.append((item[2] * 2))


df_mercado_dois = pd.DataFrame({"Categoria": categoria, "Item": it, "Valor": valor, 
"Quantidade": quantidade, "Subtotal": subtotal})

df_mercado_dois.sort_values(by=['Categoria', 'Item'], inplace=True)
print(df_mercado_dois.to_string(index=False))
