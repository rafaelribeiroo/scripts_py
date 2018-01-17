#53. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: Apos a sopa
f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#inverso = ''
# Começa no tamanho da string -1, se a string tiver 20 vai começar do 19
# Vai até a posição -1
# De -1 em -1 caractere
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
