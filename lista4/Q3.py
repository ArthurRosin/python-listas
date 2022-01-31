#Questão 3

import pandas as pd

df = pd.read_csv("fake-classrooms20.csv", sep=",")

escolha = str(input())
valores = df[(f"{escolha}")].value_counts()

print(valores)
