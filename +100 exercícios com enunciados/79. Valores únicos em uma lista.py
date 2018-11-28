# 79. Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
números = list()
while True:
    # Atribuo o valor a ser inserido na lista em uma variável
    # para se trabalhar
    n = int(input('Digite um valor: '))
    # Se o número não estiver na minha lista, vou incluir
    if n not in números:
        números.append(n)
        print(f'Valor adicionado com sucesso...')
    # Se tiver, não faz sentido incluir um dado duplicado
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 20)
números.sort()
print(f'Você digitou os valores {números}')
