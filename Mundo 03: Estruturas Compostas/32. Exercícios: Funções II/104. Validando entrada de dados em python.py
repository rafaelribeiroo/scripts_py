# 104. Crie um programa que tenha a função leiaInt(), que vai funcionar de
# forma semelhante à função input() do Python, só que fazendo a validação
# para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')


def leiaInt(valor):
    print('-' * 30)
    while True:
        valor = input('Digite um número: ')
        if valor.isnumeric() is True:
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
