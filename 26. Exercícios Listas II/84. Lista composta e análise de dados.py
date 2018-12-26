# 84. Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# > Quantas pessoas foram cadastradas.
# > Uma listagem com as pessoas mais pesadas.
# > Uma listagem com as pessoas mais leves.
lista = list()
c = 0
resp = ' '
while resp not in 'N':
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if c == 0:
        pesada = peso
        leve = peso
    else:
        if peso > pesada:
            pesada = peso
        if peso < leve:
            leve = peso
    c += 1
    lista.append()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print(lista)
