frase = 'Curso em Video Python'
#len: Length (Comprimento), nesse caso temos 21 micro-espaços
print(len(frase))
#count: Contar, Contador, nesse caso quantas x a letra O é citada na string
print(frase.count('o'))
#Contador já com o fatiamento, da posição 0 até a 13 (vídeO), quantas vezes tem o O? 1 só, lembrando que o último valor não entra pois é ignorado pelo PY
print(frase.count('o',0,13))
#Qual a posição (micro-espaço) que se encontra os caracteres 'deo'? Apenas onde começa, no caso: 11
#find: Encontrar
print(frase.find('deo'))
#E se o parâmetro passado no find não existir? Ele te retornará a posição -1, de que não existe
print(frase.find('Android'))
