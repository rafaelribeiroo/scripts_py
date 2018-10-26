# 41. A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
from datetime import date

ano_atual = date.today().year
ano_nascto = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascto
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
# elif idade > 9 and idade <= 14
# Faço dessa forma porque no if acima já é menor que 9, se não for, com
# certeza será maior, então seria redundância
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
