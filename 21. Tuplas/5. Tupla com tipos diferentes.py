pessoa = ('Rafael', 24, 'M', 80.56)
# Apagando a tupla da memória
del(pessoa)
# Como a tupla é imutável, nós não conseguimos deletar apenas um item
del(pessoa[0])
print(pessoa)
