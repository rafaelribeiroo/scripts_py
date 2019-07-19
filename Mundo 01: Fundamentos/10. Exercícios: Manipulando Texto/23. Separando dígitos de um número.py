# 23. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
# dos dígitos separados.
# Ex: Digite um número: 1834
# milhar:  1
# centena: 8
# dezena:  3
# unidade: 4

num = int(input('Informe um número: '))
# Consigo fatiar um número pela própria matemática, não precisando do SLICE
milhar = num // 1000 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10
print(f'Analisando o número {num}')
print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')
