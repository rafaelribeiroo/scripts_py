lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# Sem exibir índice
for comida in lanche:
    print(f'Eu vou comer {comida}')

print('*' * 40)

# Sempre que precisarmos dos índices dos elementos das listas (ou outros
# iteráveis), podemos usar o enumerate para construir uma estrutura
# composta por pares índice-elemento
for posição, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posição}')
print('Comi pra caramba!')

'''
Podemos fazer sem o enumerate também
for índice in range(0, len(lanche))
Chamando o item como: lanche[índice]
'''
