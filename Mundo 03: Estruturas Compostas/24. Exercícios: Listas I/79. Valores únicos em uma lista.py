# 79. Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

números = list()
while True:
    # Atribuo o valor a ser inserido em uma variável para facilitar a operação
    valor = int(input('Digite um valor: '))
    # Se o valor não estiver na minha lista
    if valor not in números:
        # Vou incluir
        números.append(valor)
        print('Valor adicionado com sucesso...')
    # Se já existir
    else:
        # Não permite inclusão
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=' * 20)
números.sort()
print(f'Você digitou os valores {números}')
