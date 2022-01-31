#Questão 3

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms19.csv", sep=",")

coluna_lida1 = str(input())
coluna_lida2 = str(input())

media_um = df[coluna_lida1].mean()
media_dois = df[coluna_lida2].mean()

print(f"media {coluna_lida1} = {media_um :.2f}")
print(f"media {coluna_lida2} = {media_dois :.2f}")

if media_um >= 6.3 and media_dois >= 6.3:
    print("As duas Medias sao maiores que 6.3")
if media_um >= 6.3 and media_dois < 6.3:
    print(f"Apenas Media {coluna_lida1} eh maior que 6.3")
if media_um < 6.3 and media_dois >= 6.3:
    print(f"Apenas Media {coluna_lida2} eh maior que 6.3")
if media_um < 6.3 and media_dois < 6.3:
    print("Nenhuma media eh maior que 6.3")
