# 60. Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

'''
1ª Solução:
from math import factorial
fatorial = factorial(n)
'''

núm = int(input('Digite um número para calcular seu fatorial: '))
c = núm
# Fator nulo de fatoração é 1
multiplicação = 1
print(f'Calculando {núm}! = ', end='')
# Vai decrementar de 1 em 1 sob o número que digitei até o 0
for contador in range(núm, 0, -1):
    # Vai mostrando a ordem decrescente do contador
    print(f'{contador}', end='')
    # Vai mostrando o x para demonstrar * enquanto o meu contador for diferente
    # de 1, quando ele chegar ao último loop, mostre o sinal de =
    print(' x ' if c != 1 else ' = ', end='')
    # A cada iteração do meu loop, vai multiplicando pelo contador
    multiplicação *= c
    # A medida que vai decrementando
    c -= 1
    # Precisamos de 2 contadores, porque enquanto um vai decrementando a
    # sequência numérica, o outro vai incrementando a sequência visual de
    # multiplicação
print(f'{multiplicação}')
