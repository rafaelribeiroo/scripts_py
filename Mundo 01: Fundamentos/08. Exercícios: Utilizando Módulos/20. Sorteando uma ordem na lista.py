# 20. O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos
# quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('1º aluno: ')
n2 = input('2º aluno: ')
n3 = input('3º aluno: ')
n4 = input('4º aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
