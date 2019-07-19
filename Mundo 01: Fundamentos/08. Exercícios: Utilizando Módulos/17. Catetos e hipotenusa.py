# 17. Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento da
# hipotenusa.

# Princípio: O quadrado da hipotenusa é igual a soma dos quadrados dos catetos
from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')
# Tem diversas soluções mas compensa nós utilizarmos as bibliotecas nativas
# Solution 1: s = (co**2) + (ca**2)
# Solution 2: h = pow(s, (1/2))
