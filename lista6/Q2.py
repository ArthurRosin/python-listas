#Questão 2

import pandas as pd
import math

df = pd.read_csv("pontos-plano-20.csv", sep=",")

def calcula_distancia_euclidiana(df, indice_p1, indice_p2, indice_p3):
    x_1, y_1 = df[["X","Y"]].loc[indice_p1]
    x_2, y_2 = df[["X","Y"]].loc[indice_p2]
    x_3, y_3 = df[["X","Y"]].loc[indice_p3]
    dx1 = (x_2 - x_1)
    dy1 = (y_2 - y_1)
    quadrado1 = (dx1**2) + (dy1**2)
    distancia1 = math.sqrt(quadrado1)

    dx2 = (x_3 - x_1)
    dy2 = (y_3 - y_1)
    quadrado2 = (dx2**2) + (dy2**2) 
    distancia2 = math.sqrt(quadrado2)

    dx3 = (x_3 - x_2)
    dy3 = (y_3 - y_2)
    quadrado3 = (dx3**2) + (dy3**2) 
    distancia3 = math.sqrt(quadrado3)

    distancia_total = (distancia1 + distancia2 + distancia3)
    return distancia_total

indice_p1 = float(input())
indice_p2 = float(input())
indice_p3 = float(input())
resultado = calcula_distancia_euclidiana(df, indice_p1, indice_p2, indice_p3)

print(f"{resultado :.2f}")
