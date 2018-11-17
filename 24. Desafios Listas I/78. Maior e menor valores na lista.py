# 78. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
números = list()
for num in range(0, 5):
    números.append(int(input(f'Digite um valor para a Posição {num}: ')))
print('=-' * 30)
print(f'Você digitou os valores {números}')
print(f'O maior valor digitado foi {max(números)} nas posições {números.index(max(números))+1}', end=' ')
