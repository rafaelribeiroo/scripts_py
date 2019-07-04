# 87. Aprimore o desafio anterior, mostrando no final:
# > A soma de todos os valores pares digitados.
# > A soma dos valores da terceira coluna.
# > O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_valor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: ')
        )
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}.')
for linha in range(0, 3):
    soma_terceira_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
for contador in range(0, 3):
    if contador == 0:
        maior_valor = matriz[1][contador]
    elif matriz[1][contador] > maior_valor:
        maior_valor = matriz[1][contador]
print(f'O maior valor da segunda linha é {maior_valor}.')
