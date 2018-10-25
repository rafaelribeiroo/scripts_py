# 25. Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
n = input('Qual é seu nome completo? ').lower()
print("Seu nome tem Silva? {}".format('silva' in n))
