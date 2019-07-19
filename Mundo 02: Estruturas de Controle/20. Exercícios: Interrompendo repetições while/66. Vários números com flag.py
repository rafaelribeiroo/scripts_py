# 66. Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = contador = 0
while True:
    núm = int(input('Digite um valor (999 para parar): '))
    if núm == 999:
        break
    contador += 1
    soma += núm
print(f'A soma dos {contador} valores foi {soma}!')
