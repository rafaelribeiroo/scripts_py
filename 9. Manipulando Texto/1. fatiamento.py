# IMPORTANTE: Lembrando que os fatiamentos mais avançados (a partir do 2º) não funcionará nas chaves do format, apenas no valor passado dentro dos parênteses em format
frase = 'Curso em Video Python'
# Exemplo
# print(frase[begin:end:step])
# Ele pega o caractere alocado na posição 9
print(frase[9])
# Ele pega do caractere alocado em 9 ate o 13
print(frase[9:13])
# E se for do 9 até um caractere que transpassa a última posição? Sem problemas, ele vai até o final e para
print(frase[9:21])
# E dessa forma? Ele pega do 9, vai até o final pulando de 2 em 2 posições
print(frase[9:21:2])
# Quando omitimos o valor antes do : dessa forma, começa do 0, como se fosse 0:5
print(frase[:5])
# Ao omitir o final, ele vai do caractere alocado na 15ª posição até o fim
print(frase[15:])
# Com 2 : seguidos começando pelo 9, ele vai até o fim da string (por não haver um digíto após 9:) pulando de 3 em 3, dev
print(frase[9::3])
# Dessa forma ele pega do início até o fim começando pelo último caractere, ou seja, string reverse (trás do início até o fim a string: RAFAEL - LEAFAR)
print(frase[::-1])
# OBS: Ao usar Django, se quiser que ele trás o último objeto cadastrado ao invés do 1º
# varList = <classe>.objects.all().order_by('-id')
