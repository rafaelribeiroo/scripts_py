# 70. Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre:
# > Qual é o total gasto na compra.
# > Quantos produtos custam mais de R$ 1000.
# > Qual é o nome do produto mais barato.

total_gasto = custa_mais_1000 = produto_barato = contador_while = 0
nome = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    # Para equiparar ao if contador == 1 no FOR, no while usamos isso
    contador_while += 1
    # Atribuindo a somatória de todos os preços no total
    total_gasto += preço
    # Se o preço for menor que 1k
    if preço > 1000:
        # Soma +1 em minha var custa_mais_1000
        custa_mais_1000 += 1
    # Se for o primeiro loop, o menor preço vai ser o 1º informado pelo user
    if contador_while == 1 or preço < produto_barato:
        produto_barato = preço
        nome = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {custa_mais_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome}, que custa R${produto_barato:.2f}')
