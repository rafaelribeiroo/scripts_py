# 80. Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o
# sort()). No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    n = int(input(f'Digite o {c}º valor: '))
    # Se ele for o 1º valor a ser inserido,
    # pode incluir tranquilamente
    if c == 0:
        lista.append(n)
    # Caso o valor passado for maior que o
    # maior atual, pode inserir após ele.
    elif n > lista[len(lista) - 1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    # Agora, se não for nem o 1º nem maior
    # que o atualmente maior, faça:
    else:
        # Posição recebe 0
        pos = 0
        # Enquanto a posição (0) for menor que o tamanho da minha lista
        while pos < len(lista):
            # Se o número a ser inserido é menor ou igual a lista na posição pos
            if n <= lista[pos]:
                # Se for menor ou igual, insiro na posição específica
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            # E vou passando de posição em posição
            pos += 1
print('=-' * 20)
print(f'Os valores digitados em ordem foram {lista}')
