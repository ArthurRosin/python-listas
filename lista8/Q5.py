# Questão 5

import pandas as pd

mercado = pd.read_csv("fake-mercado29.csv")

categoria = str(input())
lista = mercado.query(f'Categoria == "{categoria}" and Valor < 4').values.tolist()
print(f"Item; Valor; Quantidade")
for dados in lista:
    print(str(dados[1])+"; "+str(dados[2])+"; "+str(dados[3]))
