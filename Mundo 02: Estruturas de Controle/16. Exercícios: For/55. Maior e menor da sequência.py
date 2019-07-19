# 55. Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

menor_peso = maior_peso = 0
for contador in range(1, 5 + 1, 1):
    peso = float(input(f'Peso da {contador}ª pessoa: '))
    # Se for o primeiro laço, o menor e o maior vão ser congruentes
    if contador == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        # Caso o peso for maior que o da 1a pessoa cadastrada/recursivamente
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi de {maior_peso}KG')
print(f'O menor foi de {menor_peso}KG')
