# 87. Aprimore o desafio anterior, mostrando no final:
# > A soma de todos os valores pares digitados.
# > A soma dos valores da terceira coluna.
# > O maior valor da segunda linha.

mais_matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_valor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        núm = int(
            input(f'Digite um valor para [{linha}, {coluna}]: ')
        )
        if núm % 2 == 0:
            soma_pares += núm
        if coluna == 2:
            soma_terceira_coluna += núm
        if linha == coluna == 0:
            maior_valor = 0
        else:
            if linha == 1 and núm > maior_valor:
                maior_valor = núm
        mais_matriz[linha][coluna] = núm
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{mais_matriz[linha][coluna]:^5}]', end='')
    print('')
print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_valor}.')
