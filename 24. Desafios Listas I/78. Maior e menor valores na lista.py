# 78. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
listanum = []
mai = men = 0
for num in range(0, 5):
    # Quero jogar o valor dentro da variável composta
    listanum.append(int(input(f'Digite um valor para a Posição {num}: ')))
    if num == 0:
        mai = men = listanum[num]
    else:
        if listanum[num] > mai:
            mai = listanum[num]
        if listanum[num] < men:
            men = listanum[num]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
# Para cada índice e valor, printe o índice se o valor for igual
# o maior
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
    
