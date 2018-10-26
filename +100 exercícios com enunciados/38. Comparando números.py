# 38. Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    maior = num1
    print('O PRIMEIRO valor é maior'.format(maior))
elif num2 > num1:
    maior = num2
    print('O SEGUNDO valor é maior')
# ou elif num1 == num2:
else:
    print('Os dois valores são IGUAIS')
