# 93. Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante
# o campeonato.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
total_partidas = int(input(f'Quantas partidas o(a) {jogador["nome"]} jogou? '))
for contador in range(0, total_partidas):
    partidas.append(int(input(f'Quantos gols na partida {contador}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} patidas.')
for índice, valor in enumerate(jogador['gols']):
    print(f'   => Na partida {índice}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
