# Tupla com (), mas a partir do PY 3.5 os parênteses não são mais necessários
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print('{:-^30} \n\n'.format('Manipulação de TUPLA'))

# Exibe toda a tupla
print(lanche)
# Filtra apenas o 2º item: pizza
print(lanche[2])
# Do hambúrguer ao suco, pois ao trabalhar com range o último valor não entra
print(lanche[0:2])
# Do suco ao pudim
print(lanche[1:])
# Pudim
print(lanche[-1])
# Tem quantos "QUADRADINHOS" na minha TUPLA?
len(lanche)
# Do suco ao 1º (Hambúrguer)
print(lanche[-3:])
# Tuplas são imutáveis e eu posso provar
lanche[1] = 'Cerveja'
print(lanche[1])
