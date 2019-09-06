# 106. Faça um mini-sistema que utilize o Interactive Help do Python. O usuário
# vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
# palavra 'FIM', o programa se encerrará.
# OBS: use cores.

from time import sleep


def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


def meajuda(método):
    while True:
        escreva('SISTEMA DE AJUDA PyHELP')
        método = str(input('Função ou Biblioteca > '))
        if método == 'fim':
            escreva('FIM! Até logo')
            sleep(1)
            break
        else:
            escreva(f"Acessando o manual do comando '{método}'")
            sleep(1)
            help(f'{método}')
            sleep(1)


meajuda(print)
