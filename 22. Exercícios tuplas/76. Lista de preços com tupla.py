# 76. Crie um programa que tenha uma tupla única com nomes de produtos e
# seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma
# tabular.
listagem = (
    'Heineken', 4.39,
    'Glacial', 1.00,
    'Bavaria', 2.50,
    'Stella Artois', 5.20,
)
print('-' * 30)
print('{:^30}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 30)
str_listagem = listagem[::2]
int_listagem = listagem[1::2]
for c in range(0, 4):
    print(f'{str_listagem[c]:.<23}R${int_listagem[c]:>5}')
print('-' * 30)
