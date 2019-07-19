# 95. Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de
# cada jogador.

time = list()
jogador = dict()
partidas = list()

while True:
    # A cada passo leremos de um novo jogador, mas a síntaxe é inválida para
    # essa ocasião
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total_partidas = int(
        input(f'Quantas partidas o(a) {jogador["nome"]} jogou? ')
    )
    partidas.clear()
    for contador in range(0, total_partidas):
        partidas.append(
            int(input(f'Quantos gols na partida {contador + 1}? '))
        )
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 30)
print('cod ', end='')
# Cabeçalho das chaves
for chave in jogador.keys():
    print(f'{chave:<15}', end='')
print()
print('-' * 40)
for posição, elemento in enumerate(time):
    print(f'{posição:>3} ', end='')
    for dígito in elemento.values():
        # Convertemos a lista de gols para str para poder "abranger"
        print(f'{str(dígito):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        # For para percorrer a lista de gols
        for índice, gol in enumerate(time[busca]['gols']):
            print(f'   No jogo {índice + 1} fez {gol} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
