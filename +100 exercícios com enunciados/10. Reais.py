'''10. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
       e mostre quantos dólares ela pode comprar.
Considere:
    US$1,00 = R$3,27
'''
reais = float(input('Quantos Reais tem na sua carteira? '))
print('Você possui R$ {:.2f} que é equivalente a: '.format(reais))
print('US$ {:.2f}'.format((reais / 3.27)))  # U$3.27 valem  R$1.00
print('{:.2f} €'.format((reais / 3.749)))  # 3.74€ valem   R$1.00
print('{:.2f} CLP'.format(reais * 203))  # 203 CLP valem R$1.00
