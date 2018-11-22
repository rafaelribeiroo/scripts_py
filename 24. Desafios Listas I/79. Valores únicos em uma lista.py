# 79. Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
valores = list()
resp = 'S'
while resp == 'S':
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    for i, v in enumerate(valores):
        if i == 0:
            pass
        else:
            if v == valores[i]:
                print('Valor duplicado! Não vou adicionar...')
print('-=' * 20)
