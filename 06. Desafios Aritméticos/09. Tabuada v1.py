# 9. Faça um programa que leia um número Inteiro qualquer
# e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))
print('*' * 12)
print(f'{num} x {1:2} = {num*1}')
print(f'{num} x {2:2} = {num*2}')
print(f'{num} x {3:2} = {num*3}')
print(f'{num} x {4:2} = {num*4}')
print(f'{num} x {5:2} = {num*5}')
print(f'{num} x {6:2} = {num*6}')
print(f'{num} x {7:2} = {num*7}')
print(f'{num} x {8:2} = {num*8}')
print(f'{num} x {9:2} = {num*9}')
print(f'{num} x {10:2} = {num*10}')
print('*' * 12)
# O {:2} no centro é justamente para ficar alinhada as tabuadas quando o número
# informado chegar à 10ª multiplicação
