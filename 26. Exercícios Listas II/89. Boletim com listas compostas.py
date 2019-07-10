# 89. Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

ficha = list()
resp = ''
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    # Podemos utilizar o append da forma abaixo também
    # A variável composta tem 3 níveis de composição
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 26)
# No índice não vai mostrar as notas individuais, já que a lista entende
# que uma lista interna é apenas um elemento (1 índice apenas)
for índice, elemento in enumerate(ficha):
    # E pulamos ele aqui, por isso o [0] e [2]
    print(f'{índice:<4}{elemento[0]:<10}{elemento[2]:>8.1f}')
while True:
    print('–' * 35)
    opção = int(input('Mostrar notas de qual aluno? (99 interrompe): '))
    if opção == 99:
        print('FINALIZANDO...')
        break
    # - 1 porque o primeiro é 0 e o último é n - 1
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
print('<<< VOLTE SEMPRE >>>')
