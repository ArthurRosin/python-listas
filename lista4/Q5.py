#Questão 5

import pandas as pd

df = pd.read_csv("fake-classrooms06.csv", sep=",")

escolha = str(input())
moda = df[escolha].mode().max()

print(f"{moda :.2f}")
