# 22. Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas
# > O nome com todas minúsculas
# > Quantas letras ao todo (sem considerar espaços)
# > Quantas letras tem o primeiro nome
n = str(input('Nome Completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(n.upper()))
print('Seu nome em minúsculas é {}'.format(n.lower()))
# Comprimento total - Espaços em branco
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
# Pedindo pra localizar um espaço vazio da esquerda pra direita,
# saberemos quantos caracteres existem no primeiro nome.
print('Seu 1º nome tem {} letras'.format(n.find(' ')))
# separa[0], len(separa[0]  Outra forma
