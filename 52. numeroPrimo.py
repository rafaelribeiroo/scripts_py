#52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Lembrando, se ele foi divisível 2x no máximo ele é primo.
# Por 1 e por ele mesmo
# Para IDLE:
# from colorama import init
# init(convert=True)
divisivel = 0
start = '\033[31m'
end = '\033[m'
num = int(input('Digite um número: '))
for cont in range(1, num+1):
    if num % cont == 0:
        divisivel = divisivel + 1
        print(start, end='')
    else:
        print(end, end='')
    print('{} '.format(cont), end='')
print('')
print(end + 'O número {} foi divisível {} vezes'.format(num, divisivel))
if divisivel > 2:
    print(end + 'E por isso ele NÃO É PRIMO!')
else:
    print(end + 'E por isso ele É PRIMO!')
