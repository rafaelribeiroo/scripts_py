# 91. Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final, coloque
# esse dicionário em ordem, sabendo que o vencedor tirou o maior número
# no dado.

from random import randint
from time import sleep

jogadas = dict()
print('Valores sorteados: ')
for contador in range(1, 4 + 1):
    sorteio = randint(1, 6)
    print(f'   O jogador{contador} tirou {sorteio}')
    jogadas[f'jogador{contador}'] = sorteio
for
