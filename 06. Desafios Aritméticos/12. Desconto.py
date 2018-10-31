# 12. Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.
# Regrinha básica de 3, se meu produto vale 10 ele é 100%, 5% eu
# não sei ainda quanto será, então fazemos 10*5/100, 5 por cento de 10
pc = float(input('Digite o preço do produto: '))
qt = int(input('Entre com a quantidade de desconto: '))
dc = pc - (pc * qt / 100)  # Desconto
print('O desconto solicitado abaixou o ' +
      'preço do produto de {:.2f} para R${:.2f}'.format(pc, dc))
