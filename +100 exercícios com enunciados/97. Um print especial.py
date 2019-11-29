# 97. Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''Entrada:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~
Olá, mundo!
~~~~~~~~~~~
'''


def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
