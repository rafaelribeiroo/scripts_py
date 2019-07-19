# 39. Faça um programa que leia o ano de nascimento de um jovem e informe, de
# acordo com a sua idade:
# > Se ele ainda vai se alistar ao serviço militar
# > Se é a hora de se alistar
# > Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {atual}.')
sexo = input('Você é homem ou mulher? [H/M] ').upper()[0]

if sexo == 'H':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        # Se minha idade for inferior a 18, subtraia 18 na minha idade pra ver
        # quanto tempo falta pro meu alistamento
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento')
        # 2019 + (quantos anos faltam pro meu alistamento)
        ano = atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}')
else:
    print('Você está livre!')
