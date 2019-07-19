# 52. Faça um programa que leia um número inteiro e diga se ele é ou não um
# número primo. Lembrando, se ele foi divisível 2x no máximo ele é primo.
# Por 1 e por ele mesmo

núm = int(input('Digite um número: '))
divisível = 0
for contador in range(1, núm + 1):
    # Se o resto da divisão por qualquer número até chegar no optado pelo
    # usuário for 0, quer dizer que ele é divisível, então eu atribuo +1
    if núm % contador == 0:
        # Printa o número divisível na cor amarela
        print('\033[33m', end='')
        divisível += 1
    else:
        # Printa na cor vermelha
        print('\033[31m', end='')
    print(f'{contador} ', end='')
print(f'O número {núm} foi divisível {divisível} vezes')
# Confere se é primo ou não
if divisível > 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')
