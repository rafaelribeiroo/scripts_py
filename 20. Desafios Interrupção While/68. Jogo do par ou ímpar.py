# 68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint

c = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
vc = int(input('Digite um valor: '))
jogada = str(input('Par ou Ímpar? [P/I] ')).upper()
pc = randint(1, 10)
total = vc + pc
print(f'Você jogou {vc} e o computador {pc}. Total de {total}', end=' ')
while True:
    if total % 2 == 0 and jogada == 'P':
        print(f'Deu PAR')
        print('Você ganhou')
        c += 1
    elif total % 2 == 1 and jogada == 'I':
        print(f'Deu ÍMPAR')
        print('Você ganhou')
    elif total % 2 == 1 and jogada == 'P':
        print(f'Deu ÍMPAR')
        print('Você perdeu')
        break
    elif total % 2 == 0 and jogada == 'I':
        print(f'Deu PAR')
        print('Você perdeu')
        break
if c >= 1:
    print(f'Você ganhou {c} vezes')
