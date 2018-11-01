# 65. Crie um programa que leia vários números inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.
r = 'S'
maior, menor = 0, 0
while r == 'S':
    num = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        if num > maior:
            maior = num
print('Maior: {}'.format(maior))
# print('Menor: {}'.format(menor))
