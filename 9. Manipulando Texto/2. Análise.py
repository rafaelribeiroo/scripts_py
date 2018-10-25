frase = 'Curso em Video Python'
# length, nesse caso temos 21 micro-espaços
print(len(frase))
# Quantos caracteres com o parametro informado
print(frase.count('o'))
# Quantos caracteres com fatiamento (de X a Y)
print(frase.count('o', 0, 13))
# Vai buscar no indice qual o local que se encontra o parametro, o PY
# retornara a posicao apenas do 1o caractere seguido pelo restante
print(frase.find('deo'))
# Se o parametro nao for encontrado, ele retorna -1
print(frase.find('Android'))
