# 90. Faça um programa que leia nome e média de um aluno, guardando também a
# situação em um dicionário. No final, mostre o conteúdo da estrutura na
# tela.

medias = dict()

medias['nome'] = str(input('Nome: ')).capitalize()
medias['média'] = float(input(f'Média de {medias["nome"]}: '))
print(f'Média é igual a {medias["média"]:.1f}')
if medias['média'] < 7:
    medias['situação'] = 'Reprovado'
else:
    medias['situação'] = 'Aprovado'
print(f'Situação é igual a {medias["situação"]}')
