# 44. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
# print('='*10, 'LOJAS RAFAEL', '='*10)
print('{:=^40}'.format(' LOJAS RAFAEL '))
preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    ajuste = preco - (preco * 10) / 100
elif opcao == 2:
    ajuste = preco - (preco * 5) / 100
elif opcao == 3:
    ajuste = preco
    # Poderia ter atribuito o preco / 2 em ajustes? SIM! Mas, como criei uma mensagem genérica lá em baixo para tratar todos os elif, minha compra no final iria aparecer que o total seria apenas uma parcela
    parcelas = preco / 2
    print('A compra parcelada em 2x será o mesmo valor, pagando R${:.2f} a cada mês'.format(parcelas))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    ajuste = preco + (preco * 20) / 100
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcelas, ajuste / parcelas))
else:
    ajuste = preco
    print('\033[1;31;43mOpção inválida de pagamento, tente novamente\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, ajuste))
