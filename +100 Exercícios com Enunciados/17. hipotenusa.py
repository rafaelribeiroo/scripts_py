#17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#Princípio: O quadrado da hipotenusa é igual a soma dos quadrados dos catetos
from math import hypot
catetoO = float(input('Comprimento Cateto Oposto:    '))
catetoA = float(input('Comprimento Cateto Adjacente: '))
h = hypot(catetoO, catetoA)
print('A hipotenusa vai medir: {:.2f}'.format(h))
#Ou podemos fazer de outra forma, como abaixo
#s = (catetoO**2) + (catetoA**2)
#h = pow(s, (1/2))
#print(h)
#O que dara muito mais trabalho, compensa mais nós utilizarmos as bibliotecas nativas do Python 
