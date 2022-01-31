#Questão 5

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

df = pd.read_csv("gapminder_full.csv", sep=",")

def escreve_correlacao(df, nome_pais, x_col, y_col):
    dados_pais = df.query("Pais == '"+nome_pais+"'")
    x = dados_pais[x_col]
    y = dados_pais[y_col]
    m, b = np.polyfit(x, y, 1)
    y_line = m*x + b
    correlacao = x.corr(y)
    plt.scatter(x,y,30,color='blue')
    plt.plot(x, y_line, color = 'red', label='Correlação = %.3f'%correlacao)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(nome_pais)
    plt.legend()
    plt.show()
    return correlacao

nome_pais = str(input())
x_col = str(input())
y_col = str(input())

dados = escreve_correlacao(df, nome_pais, x_col, y_col)
print(f"{dados :.3f}")
