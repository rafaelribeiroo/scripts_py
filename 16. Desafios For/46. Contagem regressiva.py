# 46. Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de
# 1 segundo entre eles.
from time import sleep
# Ao invés de 0-1 poderia colocar -1 também, mesmo resultado
for c in range(10, 0 - 1, -1):
    print(c)
    sleep(0.5)
print('BUM! BUM! POOOW!')
