# 25. Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"
# no nome.

nome = input('Qual é seu nome completo? ').lower()
print(f"Seu nome tem Silva? {'silva' in nome.lower()}")
