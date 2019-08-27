# 100. Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores PARES sorteados pela função anterior.

from random import randint

números = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for contador in range(0, 5):
        números.append(randint(0, 10))
        print(números[contador], end=' ')
    print('PRONTO!')


sorteia()


def somaPar():
    print(f'Somando os valores pares de {números}, temos', end=' ')
    soma = 0
    for num in números:
        if num % 2 == 0:
            soma += num
    print(f'{soma}')


somaPar()
