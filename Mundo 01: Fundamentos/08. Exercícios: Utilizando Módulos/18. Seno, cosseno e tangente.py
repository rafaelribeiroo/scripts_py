# 18. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.

# Princípio: Devemos calcular o SENO/COSSENO/TANGENTE pelo radiano do ângulo
from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem o TANGENTE de {tangente:.2f}')
