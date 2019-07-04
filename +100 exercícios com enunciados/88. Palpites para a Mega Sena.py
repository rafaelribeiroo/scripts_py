# 88. Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O
# programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = list()
jogos = list()

print('–' * 30)
print('      JOGA NA MEGA SENA      ')
print('–' * 30)
qntde_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

# Enquanto nosso total for inferior a quantidade de jogos, não para de sortear
while total <= qntde_jogos:
    contador = 0
    # Fique em laço eterno até que o PY nos gere 6 números aleatórios
    while True:
        núm = randint(1, 60)
        # Se não houver o número sorteado na minha lista
        if núm not in lista:
            # Insira
            lista.append(núm)
            # E atribua +1 para saber se já sorteamos 6 números
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {qntde_jogos} JOGOS ', '-=' * 3)
# Trata o índice e a lista
for índice, lista in enumerate(jogos):
    print(f'Jogo {índice+1}: {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
