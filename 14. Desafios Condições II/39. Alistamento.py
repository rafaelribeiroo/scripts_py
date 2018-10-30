# 39. Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date

ano_atual = date.today().year
sexo = input('Primeiramente, você é homem ou mulher? [H/M]').upper()

if sexo == 'H':
    ano_nascto = int(input('Qual o ano de seu nascimento? '))
    idade = (ano_atual - ano_nascto)
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascto, idade, ano_atual))
    print('')
    if idade < 18:
        idade = 18 - idade
        print('Daqui {} anos você poderá se alistar no serviço militar'.format(idade))
        ano = ano_atual + idade
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        idade = idade - 18
        print('Já passou {} anos que você deveria ter se alistado'.format(idade))
        ano = ano_atual - idade
        print('Seu alistamento foi em {}'.format(ano))
    # or elif idade == 18
    else:
        print('Hora de se alistar!')
else:
    print('Você está livre!')
