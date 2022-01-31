#Questão 2

import pandas as pd

df = pd.read_csv("fake-classrooms16.csv", sep=",")
escolha = str(input())
desvio = df[escolha].values.std()

print(f"{desvio :.2f}")