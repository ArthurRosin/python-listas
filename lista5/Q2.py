#Questão 2

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms-correl10.csv", sep = ",", decimal=",")
escolha = str(input()) 

print(df[["Nota Final", escolha]])