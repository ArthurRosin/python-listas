#Questão 2

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms27.csv", sep=",")

indice_aluno = int(input())

nome = df["Nome"].loc[indice_aluno]
p_um = df["Prova 1"].loc[indice_aluno]
p_dois = df["Prova 2"].loc[indice_aluno]
trabalho = df["Trabalho"].loc[indice_aluno]
media = (p_um + p_dois + trabalho)/3

print(f"Nome: {nome}")
print(f"Prova 1: {p_um}")
print(f"Prova 2: {p_dois}")
print(f"Trabalho :{trabalho}")
print(f"media: {media :.2f}")
if media >= 6:
    print("Resultado: Aprovado")
else:
    print("Resultado: Reprovado")


