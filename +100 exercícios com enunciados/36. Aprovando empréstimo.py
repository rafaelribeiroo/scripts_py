# 36. Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo
# que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
# A prestação será a casa dividido pela quantidade de anos * por 12 meses
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end=' ')
print(f'a prestação será de R${prestação:.2f}')
# Se a prestação for inferior que 30% do meu salário bruto
if prestação <= mínimo:
    # O empréstimo está garantido
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
