# 12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Regrinha básica de 3, se meu produto vale 10 ele é 100%, 5% eu não sei ainda quanto será, então fazemos 10*5/100, 5 por cento de 10
preco = float(input('Digite o preço do produto: '))
qntde_desconto = int(input('Entre com a quantidade de desconto: '))
desconto = preco - (preco * qntde_desconto / 100)
print('O desconto de {}% abaixou o preço do produto de {:.2f} para R${:.2f}'.format(qntde_desconto, preco, desconto))
