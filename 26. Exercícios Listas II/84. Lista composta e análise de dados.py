# 84. Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# > Quantas pessoas foram cadastradas.
# > Uma listagem com as pessoas mais pesadas.
# > Uma listagem com as pessoas mais leves.
resp = ' '
while resp not in 'N':
    
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
