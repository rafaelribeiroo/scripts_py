#52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
divisivel = 0
num = int(input('Digite um número: '))
for cont in range(1, num+1):
    if num % cont == 0:
        divisivel = divisivel + 1
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{}'.format(cont), end='')
print('')
print('O número {} foi divisível {} vezes'.format(num, divisivel))
if divisivel > 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')
