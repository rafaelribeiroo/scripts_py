# 98. Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: início, fim e passo e realize a contagem. Seu programa tem que
# realizar três contagens através da função criada:
# > De 1 até 10, de 1 em 1
# > De 10 até 0, de 2 em 2
# > Uma contagem personalizada.

from time import sleep

def contagem(inicio, fim, passo):
    print('-=' * 30)
    # abs: converte qualquer número negativo para positivo
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    for contador in range(inicio, fim, passo):
        print(contador, end=' ')
        # sleep(0.2)
    print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, -2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
if end < start:
    step = -step
contagem(start, end, step)
