# 41. A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# > Até 9 anos: MIRIM
# > Até 14 anos: INFANTIL
# > Até 19 anos: JÚNIOR
# > Até 25 anos: SÊNIOR
# > Acima: MASTER

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    # No 1º if já é menor/igual a 9. Se não for, com certeza será maior, então
    # seria redundância informar elif idade > 9 and <= 14
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
