#Questão 4

import pandas as pd

df = pd.read_csv("fake-classrooms18.csv", sep=",")

escolha = str(input())

varianca =  df[escolha].values.var()
print(f"{varianca :.2f}")
