# 68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

quantidade_vitórias = 0
while True:
    jogador = int(input('Digite um valor: '))
    # Computador "pensa" de um número 0 ao 10
    # Lembrando: Ao trabalhar com range PY não pega o último valor
    computador = randint(0, 11)
    # Soma seu valor e o do computador para verificar se é ímpar ou par
    total = jogador + computador
    tipo = ' '
    # Ao escolher outra coisa sem ser I/P, sai do laço
    while tipo not in 'IP':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de '
          f'{total}', end=' ')
    # Operador ternário/Análise se é par ou ímpar o total
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    # Se você escolheu par
    if tipo == 'P':
        # E o total for par
        if total % 2 == 0:
            # Você vence
            print('Você VENCEU')
            # E soma +1 na qntde de vitória
            quantidade_vitórias += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            quantidade_vitórias += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {quantidade_vitórias} vezes.')
