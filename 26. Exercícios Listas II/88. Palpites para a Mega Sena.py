# 88. Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O
# programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

principal = []
temporária = []
contador = 1
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
qntde_palpites = int(input('Quantos jogos você quer que eu sorteie? '))
for palpite in range(1, qntde_palpites + 1):
    for sorteio in range(1, 6 + 1):
        temporária.append(randint(0, 60))
    principal.append(temporária[:])
    temporária.clear()
print(f'{" SORTEANDO 10 JOGOS ":*^30}')
for elemento in principal:
    print(f'Jogo {contador}: {elemento}')
    sleep(0.5)
    contador += 1
print('{:-^30}'.format('BOA SORTE'))
