# 49. Refaça o desafio 09, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.

número = int(input('Digite um número para ver sua tabuada: '))
for contador in range(0, 11):
    print(f'{número} x {contador:2} = {número * contador}')
