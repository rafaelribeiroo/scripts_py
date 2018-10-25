# 18. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Principio: Devemos calcular o SENO, COSSENO e TANGENTE pelo radiano do ângulo
from math import radians, sin, cos, tan
num = float(input('Qual o ângulo: '))
r = radians(num)
print('O ângulo informado foi {} e: '.format(num))
print('O Seno é: {:.2f}'.format(sin(r)))
print('O Cosseno é: {:.2f}'.format(cos(r)))
print('O Tangente é: {:.2f}'.format(tan(r)))
