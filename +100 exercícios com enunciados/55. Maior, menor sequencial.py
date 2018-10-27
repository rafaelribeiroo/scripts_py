# 55. Faça um programa que leia o peso de 5 pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.
menor, maior = 0, 0
for c in range(1, 5 + 1, 1):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    # Se for o primeiro laço, o menor e o maior vão ser congruentes.
    if c == 1:
        maior = peso
        menor = peso
    # Se for os demais laços
    else:
        # Caso o peso for maior que maior
        if peso > maior:
            maior = peso
        # Caso o peso for menor
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
