# 74. Crie um programa que vai gerar cinco números aleatórios e colocar em uma
# tupla. Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.

from random import randint

números = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)

print('Os valores sorteados foram: ', end='')
for número in números:
    print(f'{número} ', end='')

# o PY tem uma facilidade, ele trabalha com os métodos específicos das tuplas
# max e min. Inclusive, pode ser utilizado em outros locais também.
print('')
print(f'O maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
