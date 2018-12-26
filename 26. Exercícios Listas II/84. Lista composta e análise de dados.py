# 84. Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# > Quantas pessoas foram cadastradas.
# > Uma listagem com as pessoas mais pesadas.
# > Uma listagem com as pessoas mais leves.
lista = list()
galera = list()
c = 0
resp = ' '
while resp not in 'N':
    nome = str(input('Nome: '))
    peso = str(input('Peso: '))
    if c == 0:
        leve = pesada = peso
    else:
        if peso > pesada:
            pesada = peso
        if peso < leve:
            leve = peso
    c += 1
    lista.append(nome)
    lista.append(peso)
    galera.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print(f'Ao todo, você cadastrou {c} pessoas.')
print(f'O maior peso foi de {pesada}Kg. Peso de', end=' ')
for pessoa in enumerate(galera):
    if pessoa[:][1] == pesada:
        print(f'{pessoa[:][1]}', end=' ')
