# 27. Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
n = str(input('Digite seu nome completo: ')).split()
print('O 1º é: {}'.format(n[0]))
print('E o último: {}'.format(n[-1]))
# n[len(n)-1]  Outra forma
