frase = 'Rafael Ribeiro'
# [begin:end:step]

# Pega o caractere na 9ª posição
print(frase[9])  # b
# Da 9ª posição até a 13ª
print(frase[9:13])  # beir
# Se eu passar um índice além da string?
# Ele vai até o último e para
print(frase[7:15])  # Ribeiro
# Do 7 até o 14, saltando de 2 posições
print(frase[7:14:2])  # Rbio
# Ao omitir o começo, ele começa do 0
print(frase[:5])  # Rafae
# Sem especificar o fim, ele vai até o final
print(frase[10:])  # eiro
# Do 9 até o último, saltando de 3
print(frase[7::3])  # Reo
# Do início ao fim, de trás pra frente
print(frase[::-1])  # oriebiR leafaR
