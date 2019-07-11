# 93. Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante
# o campeonato.

jogador = {'nome': str(input('Nome: ')),
           'partidas': int(input('Quantas partidas? '))}
for contador in range(1, jogador['partidas'] + 1):
    jogador[f'jogo{contador}'] = int(input(f'Gols no {contador}º jogo: '))
print(jogador)
