# 96. Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a
# área do terreno.

def area(l, c):
    área = l * c
    print(f'A área de um terreno {l}x{c} é de {área:.1f}m².')

print(' Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
