# 73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois
# mostre:
# > Apenas os 5 primeiros colocados.
# > Os últimos 4 colocados da tabela.
# > Uma lista com os times em ordem alfabética.
# > Em que posição na tabela está o time da Chapecoense.
tabela = (
    'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Cruzeiro', 'Atlético-PR', 'Santos', 'Bahia',
    'Botafogo', 'Fluminense', 'Corinthians', 'Vasco da Gama', 'Sport Recife',
    'Ceará', 'Chapecoense', 'Vitória', 'América-MG', 'Paraná',
)
print('-=' * 30)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 30)
print(f'Os 5 primeiros são {tabela[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('-=' * 30)
# Dibrando a ignore do PY de não chegar ao último valor
pos_chapecó = tabela.index("Chapecoense") + 1
print(f'O Chapecoense está na {pos_chapecó}ª posição')
