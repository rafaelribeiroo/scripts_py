# 72. Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'catorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
)

resposta = ''
while resposta in 'sS':
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 >= núm >= 20:
        núm = int(input('Número inválido. Digite entre 0 e 20: '))
    print(f'Você digitou o número {contagem_extenso[núm]}')
    resposta = str(input('Deseja continuar? [s/n] ')).strip()[0]
