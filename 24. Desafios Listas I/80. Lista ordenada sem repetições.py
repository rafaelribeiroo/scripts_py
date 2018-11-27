# 80. Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o
# sort()). No final, mostre a lista ordenada na tela.
lista = list()
for c in range(0, 5):
    ser_inserido = int(input(f'Digite o {c}º valor: '))
    if c == 0:
        lista.insert(0, ser_inserido)
        print('Adicionado ao final da lista...')
    elif c == 1:
        if ser_inserido < lista[0]:
            lista.insert(0, ser_inserido)
            print('Adicionado na posição 0 da lista...')
        else:
            lista.insert(1, ser_inserido)
            print('Adicionado ao final da lista...')
    elif c == 2:
        if ser_inserido < lista[0]:
            lista.insert(0, ser_inserido)
            print('Adicionado na posição 0 da lista...')
        elif ser_inserido < lista[1]:
            lista.insert(1, ser_inserido)
            print('Adicionado na posição 1 da lista...')
        else:
            lista.insert(2, ser_inserido)
            print('Adicionado ao final da lista...')
    elif c == 3:
        if ser_inserido < lista[0]:
            lista.insert(0, ser_inserido)
            print('Adicionado na posição 0 da lista...')
        elif ser_inserido < lista[1]:
            lista.insert(1, ser_inserido)
            print('Adicionado na posição 1 da lista...')
        elif ser_inserido < lista[2]:
            lista.insert(2, ser_inserido)
            print('Adicionado na posição 2 da lista...')
        else:
            lista.insert(3, ser_inserido)
            print('Adicionado ao final da lista...')
    else:
        if ser_inserido < lista[0]:
            lista.insert(0, ser_inserido)
            print('Adicionado na posição 0 da lista...')
        elif ser_inserido < lista[1]:
            lista.insert(1, ser_inserido)
            print('Adicionado na posição 1 da lista...')
        elif ser_inserido < lista[2]:
            lista.insert(2, ser_inserido)
            print('Adicionado na posição 2 da lista...')
        elif ser_inserido < lista[3]:
            lista.insert(3, ser_inserido)
            print('Adicionado na posição 3 da lista...')
        else:
            lista.insert(4, ser_inserido)
            print('Adicionado ao final da lista...')
print(f'A lista ficou {lista}')
