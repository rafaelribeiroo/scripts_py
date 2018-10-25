tempo = int(input('Quantos anos tem seu carro? '))
# Serão 2 fluxos, dois programas dentro de um só, nunca serão executadas as 2 condições ao mesmo tempo.
'''if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')'''
# PYthon não possui operador ternário
# Mas podemos fazer atribuições, print, if, como abaixo:
print('Carro Novo!' if tempo <= 3 else 'Carro Velho!')
print('*' * 10, 'FIM', '*' * 10)
