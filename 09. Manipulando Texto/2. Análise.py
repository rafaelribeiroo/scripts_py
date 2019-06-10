frase = 'Rafael Ribeiro'

# Tamanho, 14 micro-espaços
print(len(frase))
# Qntde de caracteres com o parâmetro informado
print(frase.count('R'))
# Quantos caracteres com fatiamento (de X a Y)
print(frase.count('R', 0, 7))
# Busca no índice qual a posição que retorna (apenas do 1º caractere), o
# restante está subsequencial.
print(frase.find('be'))
# Case insensitive
print(frase.lower().find('rafa'))
# Se não localizar, ele retorna -1
print(frase.find('Pereira'))
