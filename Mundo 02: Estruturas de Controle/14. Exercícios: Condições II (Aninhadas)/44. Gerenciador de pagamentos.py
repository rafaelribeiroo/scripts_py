# 44. Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# > À vista dinheiro/cheque: 10% de desconto
# > À vista no cartão: 5% de desconto
# > Em até 2x no cartão: preço normal
# > 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS RAFAEL '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    # Decrementa 10% do valor do pedido
    total = preço - (preço * 10 / 100)
elif opção == 2:
    # No cartão subtrai 5% do valor
    total = preço - (preço * 5 / 100)
elif opção == 3:
    # Atribuo o preço a minha var total para trabalhar com ela
    total = preço
    # Em 2 vezes, divido meu total por 2
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    # Atribuo 20% sobre o valor total do produto
    total = preço + (preço * 20 / 100)
    # Pergunta ao user em quantas parcelas serão feitas
    total_parcelas = int(input('Quantas parcelas? '))
    # Divide o total em quantas parcelas o usuário escolher
    parcela = total / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R${parcela:.2f}'
          f'COM JUROS')
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
# Poderíamos ter atribuído na opção 3 o total / 2 direto na var total, mas como
# críamos essa mensagem genérica para todas as condições, realizamos assim.
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
