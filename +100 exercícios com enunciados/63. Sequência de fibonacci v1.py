# 63. Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    # O fibonacci recebe o termo 1 + termo 2
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    # A cada iteração, o termo 1 recebe o 2
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~' * 30)
