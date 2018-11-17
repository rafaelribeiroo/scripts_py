num = [2, 5, 9, 1]
# Remove o último elemento da lista, 1 no caso
# num.pop()
# Remove o elemento que está no índice 2: 9
num.pop(2)
# Ele elimina somente a 1ª ocorrência da lista
num.remove(2)
# Remove o 1º elemento
del num[0]
print(num)
'''Se ele não encontrar um número, ele dá erro
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)'''
