# 71. Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
qntde_50 = qntde_20 = qntde_10 = qntde_01 = 0
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
if valor >= 50:
    for cédula50 in range(50, valor + 1, 50):
        qntde_50 += 1
    valor -= cédula50
if valor >= 20 or valor <= 80:
    for cédula20 in range(20, valor + 1, 20):
        qntde_20 += 1
        valor -= cédula20
if valor >= 10 and valor <= 20 or valor >= 30 and valor <= 40 or valor >= 60 and valor <= 80 or valor >= 90 and valor <= 100:
    for cédula10 in range(10, valor + 1, 10):
        qntde_10 += 1
        valor -= cédula10
if valor > 0 or valor > 10:
    for cédula01 in range(1, valor + 1):
        qntde_01 += 1
        valor -= cédula01
print(f'Total de {qntde_50} cédulas de R$ 50,00')
print(f'Total de {qntde_20} cédulas de R$ 20,00')
print(f'Total de {qntde_10} cédulas de R$ 10,00')
print(f'Total de {qntde_01} cédulas de R$ 1,00')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
