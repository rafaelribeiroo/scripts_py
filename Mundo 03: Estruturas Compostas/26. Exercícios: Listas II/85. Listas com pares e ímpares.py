# 85. Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente

# Podemos declarar dessa forma também, pra não ter que sempre ficar inserindo
# uma lista dentro de outra para "matrizar"
núm = [[], []]
valor = 0
for contador in range(1, 7 + 1):
    valor = int(input(f'Digite o {contador}º valor: '))
    # Se o valor inserido for ímpar
    if valor % 2 == 0:
        # Insere na minha 1ª lista
        núm[0].append(valor)
    else:
        # Caso ímpar, insere na 2ª lista
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
