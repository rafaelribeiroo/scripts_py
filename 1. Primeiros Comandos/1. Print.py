# Abaixo, para exibir uma mensagem na tela, pode ser por meio de
# aspas simples ou aspas compostas.
print('Olá, mundo!')

# Se forem números NÃO há delimitadores.
print(7 + 4)

'''
Mas porque essa diferença?
    Mensagens: São utilizadas primordialmente para serem exibidas na tela
    Números: Para fazer cálculos
'''

# Como são dois delimitadores, ele vai concatenar as strings, retornando 74
print('7' + '4')

# Abaixo dará erro, porque o + só funciona se ambos forem do mesmo tipo
print('Ola' + 5)

# Caso queira printar com tipos diferentes, tem que colocar a vírgula
print('Olá', 5)
