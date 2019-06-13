# 76. Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

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

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for posição in range(0, len(listagem)):
    # Todos os preços estão em posições pares, então...
    if posição % 2 == 0:
        # Aloco eles à esquerda
        print(f'{listagem[posição]:.<21}', end='')
    # Os ímpares então serão os preços, correto?!
    else:
        # Deixo eles à direita com duas casas após a vírgula
        print(f'R${listagem[posição]:>7.2f}')
print('-' * 40)
