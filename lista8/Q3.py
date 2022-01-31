# Questão 3

import pandas as pd

mercado = pd.read_csv("fake-mercado01.csv")

categoria = str(input())
gasto_final = 0
lista = mercado.query(f'Categoria == "{categoria}" and Quantidade == 3').values.tolist()
print("Item; Valor; Quantidade; Gasto")
for classes in lista:
    quantidade_falta = (10 - classes[3])
    gasto = (quantidade_falta * classes[2])
    gasto_final = gasto + gasto_final
    gasto_p = (f"{gasto :.2f}")
    print(classes[1]+"; "+str(classes[2])+"; "+str(classes[3])+"; "+str(gasto_p))
print(f"Total gasto para repor os estoques: {gasto_final :.2f}")

