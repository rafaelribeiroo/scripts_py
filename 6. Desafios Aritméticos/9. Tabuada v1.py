# 9. Faça um programa que leia um número Inteiro qualquer
# e mostre na tela a sua tabuada.
n = int(input('Digite um número: '))
print('Tabuada do: {:-^20}'.format(n))
print('*' * 11)
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
print('*' * 11)
# O {:2} no centro é justamente para ficar alinhada as tabuadas
# quando o número informado chegar à 10ª multiplicação
