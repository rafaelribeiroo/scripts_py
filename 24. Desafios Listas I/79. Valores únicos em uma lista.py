# 79. Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
valores = list()
resp = 'S'
c = 0
while resp == 'S':
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    c += 1
print('-=' * 20)
print(f'Você digitou os valores {valores}')
