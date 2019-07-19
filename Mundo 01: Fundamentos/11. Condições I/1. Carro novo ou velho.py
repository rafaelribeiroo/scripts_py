tempo = int(input('Quantos anos tem seu carro? '))
# Serão dois fluxos, dois programas dentro de um só. Nunca serão executadas as
# duas condições ao mesmo tempo.

# PYthon não possui operador ternário
# Mas podemos fazer atribuições (print/if):
print('Carro Novo!' if tempo <= 3 else 'Carro Velho!')
print('*' * 10, 'FIM', '*' * 10)
