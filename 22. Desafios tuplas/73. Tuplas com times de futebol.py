# 73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois
# mostre:
# > Apenas os 5 primeiros colocados.
# > Os últimos 4 colocados da tabela.
# > Uma lista com os times em ordem alfabética.
# > Em que posição na tabela está o time da Chapecoense.

''' Como a tabela está sempre mudando, é aconselhável usarmos lista, mas como
aprendemos só tupla por ora, iremos fazer com ela, são as coleções do PY
e cada uma com sua característica, a principal da tupla é a sua
IMUTABILIDADE'''
times = (
    'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Cruzeiro', 'Atlético-PR', 'Santos', 'Bahia',
    'Botafogo', 'Fluminense', 'Corinthians', 'Vasco da Gama', 'Sport Recife',
    'Ceará', 'Chapecoense', 'Vitória', 'América-MG', 'Paraná',
)
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
# No fatiamento, ele ignora o último elemento
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 30)
# Na manipulação de strings, o PY sempre ignora o último, para deixar mais:
# 'human readable' inserimos +1 logo após definirmos a busca no index.
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
