# 49. Refaça o desafio 09, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número para ver sua tabuada: '))
for cont in range(0, 11):
    print('{} x {:2} = {}'.format(num, cont, num * cont))
