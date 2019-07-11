# 92. Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
# aposentar.

from datetime import date

pessoas = {
    'nome': str(input('Nome: ')),
    'idade': int(input('Ano de Nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 não tem): ')),
}
ano_atual = date.today().year
pessoas['idade'] = ano_atual - pessoas['idade']
if pessoas['ctps'] > 0:
    pessoas['contratação'] = int(input('Ano de contratação: '))
    pessoas['salário'] = float(input('Salário: R$ '))
    já_contribuído = ano_atual - pessoas['contratação']
    pessoas['aposentadoria'] = pessoas['idade'] + (35 - já_contribuído)
elif pessoas['ctps'] <= 0:
    pass
print('-=' * 30)
print(pessoas)
for k, v in pessoas.items():
    print(f'{k} tem o valor {v}')
