# 10. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar.
# Considere:
# US$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
print(f'Com R${real:.2f} você pode comprar US${real/3.27:.2f} ou '
      f'{real/3.749:.2f}€ ou {real*203:.2f}CLP')
