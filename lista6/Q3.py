#Questão 3

import pandas as pd
import math

df = pd.read_csv("latitude-longitude-bairros.csv", sep=";" )

def distancia_terra(lat1, lon1, lat2, lon2):
    from math import sin, cos, sqrt, atan2, radians
    lat1, lon1, lat2, lon2 = [radians(lat1), radians(lon1), radians(lat2), radians(lon2)]
    dlon, dlat = [lon2 - lon1, lat2 - lat1]
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 6371.0 * 2 * atan2(sqrt(a), sqrt(1 - a)) # 6371.0 = raio aproximado da terra

def calcula_distancia_km(df, indice_city1, indice_city2):
    latitude2, longitude2 = df[["latitude","longitude"]].loc[indice_city2]
    latitude1, longitude1 = df[["latitude","longitude"]].loc[indice_city1]
    resultado = distancia_terra(latitude1, longitude1, latitude2, longitude2)
    return resultado

indice_city1 = float(input())
indice_city2 = float(input())
resultado = calcula_distancia_km(df, indice_city1, indice_city2)

print(f"{resultado :.2f}")
