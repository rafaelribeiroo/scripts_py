# 84. Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# > Quantas pessoas foram cadastradas.
# > Uma listagem com as pessoas mais pesadas.
# > Uma listagem com as pessoas mais leves.

temporária = list()
principal = list()
maior_peso = menor_peso = 0
# Se declarar duas listas da forma abaixo, cria-se uma ligação
# temporária = principal = list()

while True:
    temporária.append(str(input('Nome: ')))
    temporária.append(float(input('Peso: ')))
    # Por dois motivos criamos duas listas
    # 1º: Para não ter dado duplicado na matriz, já que vai fazer a iteração N
    # vezes
    # 2º: Para fazer o papel do iterador do FOR (contador), já que no while não
    # trabalhamos com VARIÁVEL DE CONTROLE

    # Se não tiver nenhum dado inserido na lista principal, será meu 1º loop
    if len(principal) == 0:
        # E vou atribuir o 1º valor da lista temporária como maior e menor
        maior_peso = menor_peso = temporária[1]
    else:
        # Como eu to limpando minha lista temporária toda hora, os novos
        # valores sempre ficarão alocados na 1ª posição
        if temporária[1] > maior_peso:
            maior_peso = temporária[1]
        if temporária[1] < menor_peso:
            menor_peso = temporária[1]
    # Faço uma cópia
    principal.append(temporária[:])
    # Limpo a temporária
    temporária.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'nN':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg', end=' ')
for pessoa in principal:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]}', end=' ')
print('')
print(f'O menor peso foi de {menor_peso}Kg', end=' ')
for pessoa in principal:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}', end=' ')
