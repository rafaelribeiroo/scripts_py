from úteis import fatorial, dobro

# Quando temos muitas funções, códigos ocupando um mesmo arquivo, fica
# agradável modularizar.
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}.')
