# 60. Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120
'''
1ª Solução:
from math import factorial
f = factorial(n)

2ª Solução:
n = int(input('Fatorial: '))
c = n
f = 1
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c != 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''
n = int(input('Digite um número para \ncalcular seu Fatorial: '))
c = n
# Fator nulo de fatoração é 1, já que a multiplicação por 0 é 0
f = 1
print('Calculando {}! = '.format(n), end='')
# Enquanto o contador for maior que 0, não pare de executar
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    # Fatorial vai multiplicando o contador
    f *= c
    # E o contador vai decrementando
    c -= 1
print('{}'.format(f))
