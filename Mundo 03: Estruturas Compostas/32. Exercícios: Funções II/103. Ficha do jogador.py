# 103. Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O
# programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.


def ficha(nome='', gols=0):
    print('-' * 30)
    print(f'Nome do Jogador: {nome}')
    print(f'Número de Gols: {gols}')
    print(f'O jogador', end=' ')
    print(f'<desconhecido>' if nome == "" else f'{nome}'
          f' fez {gols} gol(s) no campeonato.')


ficha(nome='Rafael')
