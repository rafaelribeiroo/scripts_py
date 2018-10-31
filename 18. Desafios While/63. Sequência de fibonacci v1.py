# 63. Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
fibo1 = fibonacci = 0
fibo2 = termos = 1
print('~' * 25)
while termos != 0:
    termos = int(input('Quantos termos você quer mostrar? '))
    for fibo1 in range(0, termos):
        fibo1 = fibo2
        fibo2 = fibonacci
        fibonacci = fibo1 + fibo2
        print('{} → '.format(fibo2), end='')
    print('Fim')
print('~' * 25)

