#Questão 1

import pandas as pd
import numpy as np

df = pd.read_csv("pontos-plano-24.csv", sep=",")

def calcula_distancia_chebyshev(df, indice_p1, indice_p2):
    x_1, y_1 = df[["X","Y"]].loc[indice_p1]
    x_2, y_2 = df[["X","Y"]].loc[indice_p2]
    distancia = max({abs(x_2 - x_1) , abs(y_2 - y_1)})
    return distancia

indice_p1 = float(input())
indice_p2 = float(input())
resultado = calcula_distancia_chebyshev(df, indice_p1, indice_p2)

print(f"{resultado :.2f}")