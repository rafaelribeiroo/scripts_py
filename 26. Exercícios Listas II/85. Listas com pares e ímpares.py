# 85. Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente

pares_temp = []
ímpares_temp = []
principal = list()

for contador in range(1, 7 + 1):
    núm = int(input(f'Digite o {contador}° valor: '))
    if núm % 2 == 0:
        pares_temp.append(núm)
    else:
        ímpares_temp.append(núm)
principal.append(pares_temp)
principal.append(ímpares_temp)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(principal[0])}')
print(f'Os valores ímpares digitados foram: {sorted(principal[1])}')
