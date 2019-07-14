# 95. Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de
# cada jogador.

gols = list()
somatório = 0
resposta = ' '
while resposta not in 'Nn':
    print('–' * 30)
    jogador = {'nome': str(input('Nome do Jogador: '))}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for contador in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {contador}: ')))
        somatório += gols[contador]
    resposta = str(input('Quer continuar? [S/n] ')).lower()[0]
jogador['gols'] = gols[:]
jogador['total'] = somatório
