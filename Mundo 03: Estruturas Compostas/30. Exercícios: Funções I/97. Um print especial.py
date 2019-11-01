# 97. Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''Entrada:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~
Olá, mundo!
~~~~~~~~~~~
'''


def escreva(frase):
    contador = len(frase) + 2
    print('~' * contador)
    print(f'{frase:^{contador}}')
    print('~' * contador)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
