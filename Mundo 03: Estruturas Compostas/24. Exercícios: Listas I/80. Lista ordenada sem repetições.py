# 80. Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o
# sort()). No final, mostre a lista ordenada na tela.

lista = list()
# Itera 5x
for contador in range(0, 5):
    valor = int(input(f'Digite o {contador}º valor: '))
    # Podemos também fazer duas condições onde o primeiro valor printe
    # adicionado ao início e se for maior que o último adicionado ao
    # fim, mas para economizar linha fazemos dessa forma
    if contador == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    # Caso não seja maior que o último nem a primeira inserção
    else:
        # Defino a posição como 0
        posição = 0
        # Para varrermos a lista inteira
        while posição < len(lista):
            # E se o valor for menor ou igual ao que estou passando na iteração
            if valor <= lista[posição]:
                # Insiro na posição do que estava atual
                lista.insert(posição, valor)
                print(f'Adicionado na posição {posição}')
                break
            posição += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
