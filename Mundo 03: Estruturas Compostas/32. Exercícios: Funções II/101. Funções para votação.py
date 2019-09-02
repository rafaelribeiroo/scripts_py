# 101. Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou
# OBRIGATÓRIO nas eleições.

from datetime import date


def voto(ano):
    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade <= 75:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL')


print('-' * 20)
nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - nascimento
voto(idade)
