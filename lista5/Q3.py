#Questão 3

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms-correl20.csv", sep = ",", decimal=",")
escolha = str(input())

valor = df['Nota Final'].corr(df[escolha])

print("%.2f" % valor)