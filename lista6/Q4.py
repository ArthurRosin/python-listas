#Questão 4

import pandas as pd
import math

df = pd.read_csv("pontos-plano-12.csv", sep=",")

def calcula_esfera_volume(df, indice_p):
    x, y, z = df[["X","Y","Z"]].loc[indice_p]
    x = (x**2)
    y = (y**2)
    z = (z**2)
    quadrado = x + y + z
    raio = math.sqrt(quadrado)
    volume = (4/3)*(math.pi)*(raio**3)
    return volume

indice_p = float(input())
resultado = calcula_esfera_volume(df,indice_p)

print(f"{resultado :.2f}")
