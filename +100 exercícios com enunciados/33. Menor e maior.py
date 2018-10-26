# 33. Faça um programa que leia três números e mostre qual é o maior
# e qual é o menor.
n1 = int(input('Digite o 1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
# Porque receber o primeiro input em uma variável que conterá o menor?
# Nós poupamos um pouco o if, se for realmente o 1º. Deu sorte! Caso contrário,
# cairá nas demais condições dos outros if's
# Saber quando colocar algo fora da estrutura de condição é algo importante
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor é: {}'.format(menor))
print('O maior é: {}'.format(maior))
