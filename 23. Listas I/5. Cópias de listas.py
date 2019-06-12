# Peculiaridade do PY
a = [2, 3, 4, 7]

# Dessa forma, será um atalho da A. Portanto, as alterações da B afetarão
# diretamente na A
#b = a
#b[0] = 1

# Para fazer sem ligação nenhuma, temos que passar todos os valores da A pra B

# Slice completo da lista A
b = a[:]
b[0] = 1
print(f'Lista A: {a}')
print(f'Lista B: {b}')
