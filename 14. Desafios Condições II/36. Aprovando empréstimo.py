# 36. Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
# do salário ou então o empréstimo será negado
valor = float(input('Valor da casa? '))
sal = float(input('Salário do comprador: R$'))
qntdeAnos = int(input('Quantos anos de financiamento? '))
# A prestação será a casa dividido pela quantidade de anos
# multiplicado por 12 meses
prestacao = valor / (qntdeAnos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}'.format(valor, qntdeAnos, prestacao))
# Se 30% do salário dele for menor ou igual a prestação será NEGADO
if (sal * 30) / 100 <= prestacao:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
