# 63. Escreva um programa que leia um número n inteiro qualquer e mostre na
# tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

print('–' * 30)
print('Sequência de Fibonacci')
print('–' * 30)
núm = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('~' * 30)
print(f'{termo1} → {termo2}', end='')
contador = 3
while contador <= núm:
    # O fibonacci recebe o termo 1 + termo 2
    fibonacci = termo1 + termo2
    print(f' → {fibonacci}', end='')
    # A cada iteração, o termo 1 recebe o 2
    termo1 = termo2
    # E o termo 2 recebe o fibonacci
    termo2 = fibonacci
    contador += 1
print(' → FIM')
print('~' * 30)
