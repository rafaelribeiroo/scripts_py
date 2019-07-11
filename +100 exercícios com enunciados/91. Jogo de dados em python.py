# 91. Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final, coloque
# esse dicionário em ordem, sabendo que o vencedor tirou o maior número
# no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()  # or dict
print('Valores sorteados:')
for key, value in jogo.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)
# Função Itemgetter: Ranking. Se for parte 0 vai colocar como chave, 1
# para valor
# Reverse true: Vencedor em último para vencedor em primeiro
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for índice, valor in enumerate(ranking):
    print(f'   {índice+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)
