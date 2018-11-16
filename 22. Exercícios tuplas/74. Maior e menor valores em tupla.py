# Crie um programa que vai gerar cinco números aleatórios e colocar em uma
# tupla.
# Depois disso, mostre a listagem de números gerados e também indique o
# menor e o maior valor que estão na tupla.
from random import randint

lista = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)
maior = lista[0]
menor = lista[0]
print(f'Os números sorteados são: {lista}')
if lista[1] > maior:
    maior = lista[1]
if lista[2] > maior:
    maior = lista[2]
if lista[3] > maior:
    maior = lista[3]
if lista[4] > maior:
    maior = lista[4]

if lista[1] < menor:
    menor = lista[1]
if lista[2] < menor:
    menor = lista[2]
if lista[3] < menor:
    menor = lista[3]
if lista[4] < menor:
    menor = lista[4]
print(f'O maior é {maior}')
print(f'O menor é {menor}')
