# 64. Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando o flag).
num = 1
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    if num == 999:
        soma = soma - 999
print('Resultado: {}'.format(soma))
# Você digitou 4 números e a soma entre eles foi 18.
