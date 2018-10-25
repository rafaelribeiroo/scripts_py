frase = 'Curso em Video Python'
# Ele pega os espaços da sua string e dividem em várias strings, então ficam vários índices, 1 para cada palavra separada
# Tecnicamente: Split gera uma lista com todas as palavras de uma cadeia de caracteres
dividido = frase.split()
# 0 é o primeiro item da minha lista 'splitada'
print(dividido[0])
# Pega o dividido 0 (Curso) e mostre o caractere no 2º espaço (índice)
print(dividido[0][2])
# E se eu quiser unir essa lista?
juncao = '-'.join(dividido)
print(juncao)
