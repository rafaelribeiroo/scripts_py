# list define que será uma lista vazia até receber um append
valores = list()

for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# Mostra apenas os elementos
for elemento in valores:
    print(f'{elemento}...', end='')

# Mostra os elementos e o índice
for posição, elemento in enumerate(valores):
    print(f'Na posição {posição} encontrei o valor {elemento}!')
