# 92. Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
# aposentar.

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] > 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    # (dados['contratação'] + 35)  Obtendo em qual ano ele se aposenta
    # - datetime.now().year  Subtraído ao ano atual
    # dados['idade']  Pega tudo e soma a idade dele
    dados['aposentadoria'] = dados['idade'] \
        + ((dados['contratação'] + 35) -
           datetime.now().year)
print('-=' * 30)
for key, value in dados.items():
    print(f'  – {key} tem o valor {value}')
