# 70. Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre:
# > Qual é o total gasto na compra.
# > Quantos produtos custam mais de R$ 1000.
# > Qual é o nome do produto mais barato.
total = maiorqueMil = c = menor = 0
print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
while True:
    c += 1
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if preço >= 1000:
        maiorqueMil += 1
    if c == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            nome_barato = nome
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(
    f'Infelizmente, não temos nenhum produto acima de R$1.000' if maiorqueMil == 0
    else f'Temos {maiorqueMil} produto(s) custando mais de R$ 1000.00'
)
print(f'O produto mais barato foi {nome_barato}, que custa R${c:.2f}')
