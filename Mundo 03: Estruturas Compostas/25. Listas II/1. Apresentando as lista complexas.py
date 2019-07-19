teste = list()

# Inserção de elementos na lista
teste.append('Gustavo')
teste.append(40)

galera = list()
# Precisamos do fatiamento completo, caso removemos, tudo na galera emitirá
# na teste
galera.append(teste[:])

# Replace Gustavo, 40 por Maria, 22
teste[0] = 'Maria'
teste[1] = 22
