# 4. Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele
d = input('Digite algo: ')
# Minha var D é um objeto e, por isso, tem características e
# realiza funcionalidades (atributos e métodos)
print('O tipo primitivo desse valor é: ')
print(type(d))
print('')
print('Só possui espaços em branco? ', d.isspace())
print('É numérico? ', d.isnumeric())
print('É alfabético? ', d.isalpha())
print('É alfanumérico? ', d.isalnum())
print('Está em letras Maiúsculas? ', d.isupper())
print('Está em letras Minúsculas? ', d.islower())
print('Está Capitalizada? ', d.istitle())
print('É Impresso? ', d.isprintable())
print('É identificador? ', d.isidentifier())
print('É um dígito? ', d.isdigit())
print('É decimal? ', d.isdecimal())
