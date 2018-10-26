# 30. Crie um programa que leia um número inteiro e mostre na tela
# se ele é PAR ou ÍMPAR
numero = int(input('Me diga um número qualquer: '))
# Todo número ímpar fica com resto de divisão 1,
# Todo número par: 0
if numero % 2 == 0:
    print('O número {} é Par'.format(numero))
else:
    print('O número {} é Ímpar'.format(numero))
