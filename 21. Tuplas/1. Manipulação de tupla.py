# Tupla com (), mas a partir do PY 3.5 os parênteses não são mais
# necessários
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print('\n\n {:-^30} \n\n'.format(' Manipulação de TUPLA '))
# Mostra todos
print(lanche)
# Mostra pizza
print(lanche[2])
# Do hambúrguer ao suco, já que o PY não vai até o último
print(lanche[0:2])
# Do suco ao pudim
print(lanche[1:])
# Ao contrário
print(lanche[-1])
# Tem quantos QUADRADINHOS na minha TUPLA?
len(lanche)
# Do suco ao 1º (Hambúrguer)
print(lanche[-3:])
''' Provando que tuplas são imutáveis
lanche[1] = 'Cerveja'
print(lanche[1])'''
