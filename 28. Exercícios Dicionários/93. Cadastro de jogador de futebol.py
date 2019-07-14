# 93. Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante
# o campeonato.

jogador = {'nome': str(input('Nome: '))}
gols = list()
somatório = 0
partidas = int(input('Quantas partidas? '))
for contador in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {contador}: ')))
    somatório += gols[contador]
jogador['gols'] = gols[:]
jogador['total'] = somatório
print('-=' * 30)
print(f'{jogador}')
print('-=' * 30)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for pos, valor in enumerate(gols):
    print(f'    => Na partida {pos}, fez {gols[pos]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
