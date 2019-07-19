# 82. Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.

núm = list()
pares = list()
ímpares = list()

while True:
    núm.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
for índice, valor in enumerate(núm):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        ímpares.append(valor)

print('-=' * 20)
print(f'A lista completa é {núm}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
