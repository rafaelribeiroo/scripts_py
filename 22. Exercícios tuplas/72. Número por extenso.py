# 72. Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.
extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
)
núm = int(input('Digite um número entre 0 e 20: '))
while True:
    if núm > 20 or núm < 0:
        núm = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print('Você digitou o número {}'.format(extenso[núm]))
