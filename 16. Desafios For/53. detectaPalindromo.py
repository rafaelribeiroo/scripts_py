#53. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: Apos a sopa
f = str(input('Digite uma frase: ')).upper()
tam = len(f)
unir = f.replace(' ', '')[::-1]
for c in range(tam, 0, -1):
    unir = unir[::-1]
    print('O inverso de {} é {}'.format(f, unir))
