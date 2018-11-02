# 65. Crie um programa que leia vários números inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.
r = 'S'
maior, menor = 0, 99999
qntde_num = soma = 0
while r == 'S':
    num = int(input('Digite um número: '))
    qntde_num += 1
    soma += num
    r = str(input('Quer continuar? [S/N] ')).upper()
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / qntde_num
print('Você digitou 4 números e a média foi {}'.format(media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
