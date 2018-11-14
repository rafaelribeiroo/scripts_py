# 71. Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
qntde_50 = qntde_20 = 0
c50 = 0
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
for cédula50 in range(50, valor + 1, 50):
    qntde_50 += 1
for cédula20 in range(cédula50, valor, 20):
    qntde_20 += 1
print(f'Total de {qntde_50} cédulas de R$50')
print(f'Total de {qntde_20} cédulas de R$20')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
