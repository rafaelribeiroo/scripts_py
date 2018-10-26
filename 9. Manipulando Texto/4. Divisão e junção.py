frase = 'Curso em Video Python'
# Ele pega os espaços da sua string e divide em várias strings,
# então ficam vários índices, 1 para cada palavra.
# Tecnicamente: Split gera uma lista com todas as palavras de uma
# cadeia de caracteres
dividido = frase.split()
# Primeiro item da lista
print(dividido[0])
# Primeiro item da lista com slice no 2º caractere, retorna r (começa do 0)
print(dividido[0][2])
# E se eu quiser unir essa lista?
juncao = '-'.join(dividido)
print(juncao)
