# 94. Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# > Quantas pessoas foram cadastradas;
# > A média de iadde do grupo;
# > Uma lista com todas as mulheres;
# > Uma lista com todas as pessoas com idade acima da média.

resposta = ' '
contador = soma_idades = 0
nome_mulheres = []
listão = list()
while resposta not in 'Nn':
    pessoas = {'nome': str(input('Nome: ')),
               'sexo': str(input('Sexo: [M/F] ')).upper()[0],
               'idade': int(input('Idade: '))}
    soma_idades += pessoas["idade"]
    contador += 1
    if pessoas['sexo'] == 'F':
        nome_mulheres.append(pessoas['nome'])
    listão.append(pessoas)
    resposta = str(input('Deseja continuar? [s/n] '))
print('-=' * 30)
print(f'– O grupo tem {contador} pessoas.')
média = soma_idades / contador
print(f'– A média de idade é de {média:.2f} anos.')
print(f'– As mulheres cadastradas foram:', end=' ')
for nome in nome_mulheres:
    print(f'{nome}', end=' ')
print()
print('– Lista das pessoas que estão acima da média: ')
for posição, elemento in enumerate(listão):
    if listão[posição]["idade"] > média:
        print(f'{listão[posição]}')
