# 19. Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
# escolhido.

from random import choice

print('*' * 30)
print('S O R T  E I O   DE   A L U N O S')
print('*' * 30)
n1 = input('1º aluno: ')
n2 = input('2º aluno: ')
n3 = input('3º aluno: ')
n4 = input('4º aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido foi: {}'.format(escolhido))
