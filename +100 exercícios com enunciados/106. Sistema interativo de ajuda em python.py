# 106. Faça um mini-sistema que utilize o Interactive Help do Python. O usuário
# vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
# palavra 'FIM', o programa se encerrará.
# OBS: use cores.

from time import sleep

c = ('\033[m',  # 0 – Sem cor
     '\033[0;30;41m',  # 1 – Vermelho
     '\033[0;30;42m',  # 2 – Verde
     '\033[0;30;43m',  # 3 – Amarelo
     '\033[0;30;44m',  # 4 – Azul
     '\033[0;30;45m',  # 5 – Roxo
     '\033[7;30m'  # 6 – Branco
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    # Devemos colocar a condição de finalizar o programa no início,
    # caso não queira ver nada, já sai na hora
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
