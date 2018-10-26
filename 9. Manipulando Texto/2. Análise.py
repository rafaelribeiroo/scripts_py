frase = 'Curso em Video Python'
# length, nesse caso temos 21 micro-espaços
print(len(frase))
# Quantos caracteres com o parâmetro informado
print(frase.count('o'))
# Quantos caracteres com fatiamento (de X a Y)
print(frase.count('o', 0, 13))
# Vai buscar no indice qual o local que se encontra o parâmetro, o PY
# retornará a posição apenas do 1º caractere, o restante está subsequencial.
print(frase.find('deo'))
# Sem diferenciação de Camel Case:
# .lower().find('deo'))
# Se o parâmetro não for encontrado, ele retorna -1
print(frase.find('Android'))
