#Questão 1

import random as rd
seed = int(input())
rd.seed(seed)

quant = 1

escolha = rd.randint(1,6)
while escolha != 6:
    escolha = rd.randint(1,6)
    if escolha != 6:
        quant += 1

print(f"Foram necessárias {quant} jogadas até aparecer o lado {escolha}")

