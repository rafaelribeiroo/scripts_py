# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
# não continuar. No final, mostre:
# > Quantas pessoas tem mais de 18 anos.
# > Quantos homens foram cadastrados.
# > Quantas mulheres tem menos de 20 anos.
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
