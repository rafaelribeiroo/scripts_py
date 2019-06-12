# 84. Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# > Quantas pessoas foram cadastradas.
# > Uma listagem com as pessoas mais pesadas.
# > Uma listagem com as pessoas mais leves.
lista = list()
galera = list()
contador = 0
resposta = ' '

while resposta not in 'N':
    nome = str(input('Nome: '))
    peso = str(input('Peso: '))
    if contador == 0:
        leve = pesada = peso
    else:
        if peso > pesada:
            pesada = peso
        if peso < leve:
            leve = peso
    contador += 1
    lista.append(nome)
    lista.append(peso)
    galera.append(lista[:])
    lista.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')

print(f'O maior peso foi de {pesada}Kg. Peso de', end=' ')
for item in enumerate(galera):
    # Ao colocar enumerate >>
    # 1º [1]: 0 será o índice da minha lista que está no 1
    # 2º [1]: Meu primeiro dado é o nome, o segundo que é o peso
    if item[1][1] == pesada:
        print(f'{item[1][0]}', end=' ')

print(f'\nO menor peso foi de {leve}Kg. Peso de', end=' ')
for item in enumerate(galera):
    if item[1][1] == leve:
        print(f'{item[1][0]}', end=' ')
