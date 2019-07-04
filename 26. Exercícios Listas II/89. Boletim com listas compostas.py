# 89. Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

resposta = ''
temp = list()
principal = list()
while resposta in 'Ss':
    # Alimentação
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    media = (temp[1] + temp[2]) / 2
    temp.append(media)
    principal.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? [S/n] ')).lower().strip()[0]
print('-=' * 30)
print('No. NOME         MÉDIA')
print('–' * 25)
for pos, elemento in enumerate(principal):
    print(f'{pos}', end='')
    for pos_item, item in enumerate(elemento):
        if pos_item == 0:
            print(f'{item:^12}', end='')
        if pos_item == 3:
            print(f'{item:>7}')
print('–' * 30)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for pos_lista, lista in enumerate(principal):
        if notas == pos_lista:
            print(f'O aluno {principal[notas][0]} tem as notas'
                  f'{principal[notas][1:3]}')
    if notas == 999:
        break
