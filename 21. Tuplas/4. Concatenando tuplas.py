a = (2, 5, 4)
b = (5, 8, 1, 2)

# Quando somamos duas tuplas, ele cria uma 3ª concatenando ambas
c = a + b
print(c)

# Quantas vezes o número 5 apareceu na tupla C
print(c.count(5))  # 2
# E quando não há um item?
print(c.count(9))  # 0
# Em qual posição está meu argumento 8?
print(c.index(8))  # 4
# Minha 1ª ocorrência de 5 é na posição 0, mas e se eu quiser pegar
# na próxima posição? Você insere uma vírgula e informa de onde vai
# começar a buscar
print(c.index(5, 1))
