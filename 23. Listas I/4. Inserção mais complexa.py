# list define que será uma lista vazia até receber um append
valores = list()
'''valores.append(5)
valores.append(9)
valores.append(4)'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

#for elemento in valores:
#    print(f'{elemento}...', end='')

# O enumerate pega tanto o índice quanto o elemento
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
