#Questão 4

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms23.csv", sep=",")

indice_aluno = int(input())

nome = df["Nome"].loc[indice_aluno]
p_um = df["Prova 1"].loc[indice_aluno]
p_dois = df["Prova 2"].loc[indice_aluno]
trabalho = df["Trabalho"].loc[indice_aluno]
media = (p_um + p_dois + trabalho)/3

if 10 >= media >= 9.00: conceito = ("A")
if 9 > media >= 7.10: conceito = ("B")
if 7.10 > media >= 5.90: conceito = ("C")
if 5.90 > media >= 4.30: conceito = ("D")
if 4.30 > media : conceito = ("F")

print(f"Nome: {nome}")
print(f"Prova 1: {p_um}")
print(f"Prova 2: {p_dois}")
print(f"Trabalho : {trabalho}")
print(f"media: {media :.2f}")
print(f"Conceito: {conceito}")
