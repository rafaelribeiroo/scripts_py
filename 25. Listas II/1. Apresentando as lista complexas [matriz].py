teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
# Vai aparecer Maria nas 2 estruturas, porque o que faço em uma
# lista duplicada, remete nas duas, para tirar qualquer ligação
# precisamos do fatiamento completo, como abaixo.
galera.append(teste[:])

print(galera)
