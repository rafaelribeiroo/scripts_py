# 4. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele

# Minha var 'dígito' é um objeto e, por isso, tem características e realiza
# funcionalidades (atributos e métodos)
dígito = input('Digite algo: ')

print('O tipo primitivo desse valor é: ')
print(type(dígito))

print('\nSó possui espaços em branco? ', dígito.isspace())
print('É numérico? ', dígito.isnumeric())
print('É alfabético? ', dígito.isalpha())
print('É alfanumérico? ', dígito.isalnum())  # Possui letras e num
print('Está em letras maiúsculas? ', dígito.isupper())
print('Está em letras minúsculas? ', dígito.islower())
print('Está capitalizada? ', dígito.istitle())
print('É impresso? ', dígito.isprintable())
print('É identificador? ', dígito.isidentifier())
print('É um dígito? ', dígito.isdigit())
print('É decimal? ', dígito.isdecimal())
