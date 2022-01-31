#Questão 4

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms-correl02.csv", sep=",")

coluna_lida1 = str(input())
coluna_lida2 = str(input())
x = float(input())

correlacao = df[coluna_lida1].corr(df[coluna_lida2])
correlacao_m = abs(correlacao)

a, b = np.polyfit(df[coluna_lida1], df[coluna_lida2], deg = 1)
y = a*x + b

if correlacao_m < (0.43):
    resposta = ("Correlação < 0.43. Atenção com a predição!")
if correlacao_m >= (0.76):
    resposta = ("Correlação >= 0.8")
if correlacao_m >= (0.43) and correlacao_m < (0.76):
    resposta = ("Correlação < 0.73. Atenção com a predição!")

print(f"Correlação entre {coluna_lida1} e {coluna_lida2} = {correlacao :.2f}")
print(f"Equação: y = {a :.2f}x + {b :.2f}")
print(f"Predição de {coluna_lida1} para {coluna_lida2} = {x :.2f} é {y:.2f}. {resposta}")
