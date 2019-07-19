# 95. Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de
# cada jogador.

pessoa = dict()
galera = list()

while True:
    gols = list()
    # Definimos a soma dentro do While porque a cada iteração ela iria
    # armazenar o último valor de soma, agora iterando sempre, ela vai
    # passar a valer 0 para somar o total de gols de cada pessoa.
    soma = 0
    print('–' * 50)
    pessoa['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {pessoa["nome"]} jogou? '))
    for contador in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {contador}? ')))
        soma += gols[contador]
    pessoa['gols'] = gols[:]
    pessoa['total'] = soma
    # Não se torna necessário já que inserimos a lista vazia a cada iteração
    # gols.clear()
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('–' * 50)
print(galera)
print('–' * 50)
print(' cód nome       gols               total')
for índice, elemento in enumerate(galera):
    print(f'{índice:>4} {galera[índice]["nome"]:<10} '
          f'{galera[índice]["gols"]} {galera[índice]["total"]:^30}')
print()
while True:
    print('–' * 50)
    opção = int(input('Deseja ver o registro de algum? '))
    if opção == len(galera) - 1:
        print(f'ERRO! Não existe o índice {opção} em nossos registros')
    elif opção == 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {galera[opção]["nome"]}')
        for contador in range(0, len(galera[opção]["gols"])):
            print(f'No {contador+1}º jogo, fiz '
                  f'{galera[opção]["gols"][contador]} gols.')
