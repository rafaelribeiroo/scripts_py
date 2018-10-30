# 28. Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# Randomizar um número int
from random import randint
from time import sleep

print('-*' * 5, 'ADIVINHAÇÃO v1.0', '-*' * 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
print('')
# Faz o computador sortear um número Inteiro entre 0 e 5
n = randint(0, 5)
a = int(input('Em que número eu pensei? '))
print('Aguarde... Processando')
# Faz o interpretador esperar 2 segundos
sleep(2)
print('> Parabéns, você conseguiu me vencer!' if a==n else '> Ganhei, eu pensei no número {} e não no {}!'.format(n, a))
