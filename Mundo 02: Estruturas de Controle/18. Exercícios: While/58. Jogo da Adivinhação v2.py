# 58. Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

# O Randint não ignora o final, vai até o 10
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    # Se o palpite do jogador e pc forem os mesmos, saia do loop
    if jogador == computador:
        acertou = True
    else:
        # Sendo abaixo
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        # Sendo acima
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} palpites')
