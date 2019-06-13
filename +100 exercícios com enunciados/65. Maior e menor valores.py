# 65. Crie um programa que leia vários números inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

resposta = 'S'
somatório = contador = maior = menor = média = 0
while resposta in 'Ss':
    núm = int(input('Digite um número: '))
    somatório += núm
    contador += 1
    # Se a quantidade de números for igual a 1, será o 1º loop
    if contador == 1:
        # Então, o maior e o menor serão o mesmo valor
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
# A média é o totalitário dividido pela quantidade de números informados
média = somatório / contador
print(f'Você digitou {contador} números e a média foi {média:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
