num = [2, 5, 9, 1]

# Remove o elemento que está na posição 2, quando não especifica remove último
num.pop(2)
# Ele elimina somente um valor (1ª ocorrência)
num.remove(2)
# Remove o 1º elemento
del num[0]
# Condição: Se existe o valor 5 na lista
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
