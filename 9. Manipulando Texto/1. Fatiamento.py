# IMPORTANTE: Lembrando que os fatiamentos mais avançados
# não funcionará nas chaves do format, apenas na referência
# das variáveis.
frase = 'Curso em Video Python'
# Modelo: [begin:end:step]
# Pega o caractere na 9ª posição
print(frase[9])
# Da 9ª posição até a 13ª
print(frase[9:13])
# Se eu passar um índice além da string?
# Ele vai até o último e para
print(frase[9:21])
# Vai do caractere 9 até o 19, pulando 2 em 2 posições
print(frase[9:21:2])
# Ao omitir o começo, ele começa do 0
print(frase[:5])
# Ao omitir o fim, ele vai até o final
print(frase[15:])
# # Do caractere 9 até o último, pulando de 3 em 3
print(frase[9::3])
# Do início ao fim, de trás pra frente
print(frase[::-1])
