# 55. Faça um programa que leia o peso de 5 pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.
maior = 0
menor = 999999
for c in range(1, 5 + 1, 1):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
