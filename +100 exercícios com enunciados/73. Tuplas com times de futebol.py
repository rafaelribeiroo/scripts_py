# 73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# > Apenas os 5 primeiros colocados.
# > Os últimos 4 colocados da tabela.
# > Uma lista com os times em ordem alfabética.
# > Em que posição na tabela está o time da Chapecoense.

''' TUPLA/LISTA/DICIONÁRIOS são as COLEÇÕES do PY e cada uma com sua
característica, a principal da tupla é a sua IMUTABILIDADE'''
times = (
    'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Cruzeiro', 'Atlético-PR', 'Santos', 'Bahia',
    'Botafogo', 'Fluminense', 'Corinthians', 'Vasco da Gama', 'Sport Recife',
    'Ceará', 'Chapecoense', 'Vitória', 'América-MG', 'Paraná',
)

print('-=' * 15)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 15)

print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
# O primeiro é 0, então inserimos +1 no índice para ser mais "human readable"
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
