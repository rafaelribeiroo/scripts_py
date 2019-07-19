# 30. Crie um programa que leia um número inteiro e mostre na tela se ele é PAR
# ou ÍMPAR

número = int(input('Me diga um número qualquer: '))
# Todo número ímpar fica com resto de divisão 1
# Par: 0
resultado = número % 2
if resultado == 0:
    print(f'O número {número} é PAR')
else:
    print(f'O número {número} é ÍMPAR')
