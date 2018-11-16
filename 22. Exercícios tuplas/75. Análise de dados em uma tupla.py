# 75. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# > Quantas vezes apareceu o valor 9.
# > Em que posição foi digitado o primeiro valor 3.
# > Quais foram os números pares.
c = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (
    n1, n2, n3, n4
)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
# Um problema do index, é que se ele não encontrar o parâmetro informado ele
# retorna erro ao invés de 0 ou algo do tipo, então temos uma tratativa
# nomeada Try/Except para tratar os erros e mostrar uma mensagem mais amigável
try:
    print(f'O valor 3 apareceu na {tupla.index(3, 0)+1}ª posição')
except ValueError:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for num in tupla:
    if num % 2 == 0:
        print(f'{num} ', end='')
