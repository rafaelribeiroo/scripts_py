# 82. Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = list()
lista_pares = list()
lista_ímpares = list()
resp = ' '
c = 0
while resp not in 'N':
    lista.append(int(input('Digite um número: ')))
    if lista[c] % 2 == 0:
        lista_pares.append(lista[c])
    else:
        lista_ímpares.append(lista[c])
    c += 1
    resp = str(input('Quer continuar? ')).strip().upper()[0]
print('-=' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_ímpares}')
