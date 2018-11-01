# 64. Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).
# Todas as variáveis passam a valer 0
núm = cont = soma = 0
# Porque o mesmo código em duas linhas?
# O flag não vai ser somado se for 999, porque se for 999, ele vai sair
# direto, e não somar.
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
