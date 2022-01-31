# Questão 4

import pandas as pd

mercado = pd.read_csv("fake-mercado22.csv")

lista = []
gasto_total = 0

print("Item; Valor; Quantidade; Subtotal")
for produtos in range(12):
    item = str(input())
    planilha = mercado.query(f'Item == "{item}"').values.tolist()
    lista.append(planilha)
for itens in lista:
    for dados in itens:
        if dados[3] >= 4:
            form = (dados[2] * 4)
            gasto_total = gasto_total + form
            form_p = (f"{form :.2f}")
            print(dados[1]+"; "+str(dados[2])+"; 4; "+str(form_p))
        else:
            form = (dados[2] * dados[3])
            gasto_total = gasto_total + form
            form_p = (f"{form :.2f}")
            print(dados[1]+"; "+str(dados[2])+"; "+str(dados[3])+"; "+str(form_p))
print(f"Total gasto na compra: {gasto_total :.2f}")
