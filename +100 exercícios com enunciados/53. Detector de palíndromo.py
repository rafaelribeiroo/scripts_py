# 53. Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços.
# Ex: Apos a sopa

frase = str(input('Digite uma frase: ')).strip().upper()
# Segmenta cada frase em uma lista
palavras = frase.split()
# Reúne todas as frases removendo os espaços
junto = ''.join(palavras)
# Printa cada caractere de trás pra frente
inverso = junto[::-1]

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# Outra solução:
'''
Começa no último índice da minha lista
Vai até o -1
De -1 em -1 caractere
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''
