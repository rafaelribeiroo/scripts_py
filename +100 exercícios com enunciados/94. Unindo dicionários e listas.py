# 94. Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# > Quantas pessoas foram cadastradas;
# > A média de iadde do grupo;
# > Uma lista com todas as mulheres;
# > Uma lista com todas as pessoas com idade acima da média.

pessoa = dict()
# Criamos uma lista para termos múltiplos dicionários "com o mesmo índice"
galera = list()
soma_idades = média = 0

while True:
    # A instrução abaixo se torna desnecessária, já que no dicionário, é
    # impossível inserir mais de 1 elemento com o mesmo índice literal
    # (ele sobreescreve)
    # pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    # Um "truque" para filtrar apenas as "respostas corretas"
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idades += pessoa['idade']
    galera.append(pessoa.copy())
    # galera = pessoa[:]
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma_idades / len(galera)
# 5 casas ao todo com 2 após o ponto
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for pessoa in galera:
    if pessoa['idade'] >= média:
        print('    ')
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<< ENCERRADO >>')
