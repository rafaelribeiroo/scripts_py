# 64. Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag). Todas as variáveis
# passam a valer 0

núm = contador = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    # Atribui o primeiro valor se for a primeira iteração, nas demais, soma ao
    # anterior
    soma += núm
    contador += 1
    núm = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {contador} números e a soma entre eles foi {soma}')
