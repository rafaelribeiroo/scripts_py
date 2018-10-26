# 16. Crie um programa que leia um número Real qualquer pelo teclado e
# mostre na tela a sua porção Inteira.
'''
Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6
'''
from math import floor, trunc

num = float(input('Digite um número: '))
print('Serão três opções que podem obter o mesmo resultado')
print('O número {} tem a porçao Inteira: '.format(num))
print('{}: Floor do Math'.format(floor(num)))
# ou
print('{}: Truncate do Math'.format(trunc(num)))
# ou, sem bibliotecas adicionais
print('{}: Sem Módulos, apenas a conversão do Python'.format(int(num)))
