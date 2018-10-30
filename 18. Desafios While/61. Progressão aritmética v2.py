# 62. Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura
# while.
print('Gerador de PA')
print('-=' * 9)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
# Décimo: Pra estipular até onde meu primeiro termo deve ir
# Pra condição do while não ficar errônea como abaixo
# while pt < pt + 10 (que o exercício pede)
dc = pt + (10) * rz
# Enquanto o primeiro termo for inferior ao décimo
while pt < dc:
    print(pt, end=' → ')
    pt = pt + rz
print('FIM')
