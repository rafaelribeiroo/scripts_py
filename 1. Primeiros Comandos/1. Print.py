# Abaixo, para exibir uma mensagem na tela, pode ser por meio de
# aspas simples ou aspas compostas.
print('Olá, mundo!')

# Se forem números NÃO há delimitadores.
print(7 + 4)

'''
Mas porque essa diferenca?
    Mensagens: Sao utilizadas primordialmente para serem exibidas na tela
    Numeros: Para fazer calculos
'''

# Como ha dois delimitadores, ele vai concatenar as strings, retornando 74
print('7' + '4')

# Abaixo dara erro, porque o + so funciona se ambos forem do mesmo tipo
print('Ola' + 5)

# Caso queira printar com tipos diferentes, tem que colocar a virgula
print('Olá', 5)
