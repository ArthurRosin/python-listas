#Questão 2

import random as rd

seed = int(input())
rd.seed(seed)
inicio = float(input())
aposta = float(input())
simula = int(input())
quant_vit = 0
quant_der = 0

for rodadas in range(0,simula):
    valor = rd.randint(9,10)
    if valor == 9:
        inicio += (aposta*2)
        quant_vit += 1
    elif valor == 10:
        inicio -= (aposta)
        quant_der += 1

print(f"O jogador faliu {quant_der}")
print(f"O jogador prosperou {quant_vit}")
if quant_vit > quant_der:
    print("Numero de vezes que o jogador faliu eh menor que o numero de vezes que prosperou")
else:
    print("Numero de vezes que o jogador prosperou eh menor que o numero de vezes que faliu")