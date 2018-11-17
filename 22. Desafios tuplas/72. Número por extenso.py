# 72. Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.
cont = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'catorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
)
resp = ''
while resp in 'Ss':
    núm = int(input('Digite um número entre 0 e 20: '))
    while núm < 0 or núm > 20:
        núm = int(input('Tente novamente: '))
    print('Você digitou o número {}'.format(cont[núm]))
    resp = str(input('Deseja prosseguir? ')).strip()[0]
