#Questão 1

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms-correl20.csv", sep = ",", decimal=",")
entrada = input()
x = (df[entrada]).values
x = df[entrada].corr(df['Nota Final'])

print(f"{x :.2f}")
