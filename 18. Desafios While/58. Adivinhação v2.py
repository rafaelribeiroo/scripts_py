# 58. Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint

# O Randint não ignora o final, vai até o 10
pc = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if jogador == pc:
        acertou = True
    # Se jogada do jogador for diferente do pc
    else:
        # Sendo abaixo
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        # Sendo acima
        elif jogador > pc:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas'.format(tentativas))
