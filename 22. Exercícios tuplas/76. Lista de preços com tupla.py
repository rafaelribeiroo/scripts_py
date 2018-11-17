# 76. Crie um programa que tenha uma tupla única com nomes de produtos e
# seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma
# tabular.
listagem = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)
print('-' * 30)
print('{:^30}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<21}', end='')
    else:
        # Provando que há forma de abranger o espaçamento da var
        # definindo quantas casas após o ponto
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 30)
