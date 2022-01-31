#Questão 1

import pandas as pd
import numpy as np
import math

df = pd.read_csv("fake-classrooms30.csv", sep=",")

def calculaNota(linha):
    return(linha["Prova 1"] + linha["Prova 2"] + linha["Trabalho"])/3
   
df["Nota"] = df.apply(calculaNota, axis=1)

def formataConceito(df):
    hist = df["Conceito"].value_counts()
    resp = ""
    if "A" in hist.keys():
        resp += "A: %d\n" % hist["A"]
    if "B" in hist.keys():
        resp += "B: %d\n" % hist["B"]
    if "C" in hist.keys():
        resp += "C: %d\n" % hist["C"]
    if "D" in hist.keys():
        resp += "D: %d\n" % hist["D"]
    if "F" in hist.keys():
        resp += "F: %d\n" % hist["F"]
    return str(resp)

def condicoes(df, nota_a, nota_b, nota_c, nota_d):
    media = df["Nota"]
    if 10 >= media >= nota_a: return ("A")
    if nota_a > media >= nota_b: return ("B")
    if nota_b > media >= nota_c: return ("C")
    if nota_c > media >= nota_d: return ("D")
    if nota_d > media:return ("F")

nota_a = float(input())
nota_b = float(input())
nota_c = float(input())
nota_d = float(input())

df["Conceito"] = df.apply(condicoes, axis=1, args = [nota_a, nota_b, nota_c, nota_d])

print(formataConceito(df))
