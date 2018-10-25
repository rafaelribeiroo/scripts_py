# 30. Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
numero = int(input('Me diga um número qualquer: '))
# resultado = numero % 2, e posso comparar o resultado no if com o número 0
# Todo número ímpar dá resultado 1, todo número par: 0
if numero % 2 == 0:
    print('O número {} é Par'.format(numero))
else:
    print('O número {} é Ímpar'.format(numero))
