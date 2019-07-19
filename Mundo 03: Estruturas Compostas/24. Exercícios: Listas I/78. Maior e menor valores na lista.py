# 78. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

listanúm = []
maior = menor = 0
for núm in range(0, 5):
    # Quero jogar o valor dentro da variável composta
    listanúm.append(int(input(f'Digite um valor para a posição {núm}: ')))
    if núm == 0:
        maior = menor = listanúm[núm]
    else:
        if listanúm[núm] > maior:
            maior = listanúm[núm]
        if listanúm[núm] < menor:
            menor = listanúm[núm]

print('=-' * 30)
print(f'Você digitou os valores {listanúm}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
# Para cada índice e valor...
for índice, elemento in enumerate(listanúm):
    if elemento == maior:
        # Printe o índice se o elemento for igual o maior
        print(f'{índice}... ', end='')

print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for índice, elemento in enumerate(listanúm):
    if elemento == menor:
        print(f'{índice}... ', end='')
