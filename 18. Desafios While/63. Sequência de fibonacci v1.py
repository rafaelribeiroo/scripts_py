# 63. Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
# 1o termo
t1 = t3 = 0
# 2o termo
t2 = n = 1
print('~' * 25)
while n != 0:
    n = int(input('Quantos termos você quer mostrar? '))
    for t1 in range(0, n):
        t1 = t2
        t2 = t3
        # Somar os dois termos anteriores pra obter o próximo
        t3 = t1 + t2
        print('{} → '.format(t2), end='')
    print('Fim')
print('~' * 25)
