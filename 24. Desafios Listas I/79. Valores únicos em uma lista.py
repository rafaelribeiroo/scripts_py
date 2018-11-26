# 79. Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
listanum = list()
c = 0
resp = ' '
while resp not in 'N':
    num_a_ser_inserido = int(input(f'Digite o {c}o. valor: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if num_a_ser_inserido in listanum:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso.')
        listanum.append(num_a_ser_inserido)
    c += 1
print('-=' * 20)
print(f'Você digitou os valores {sorted(listanum)}')
