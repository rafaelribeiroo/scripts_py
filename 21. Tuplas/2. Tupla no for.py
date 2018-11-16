lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print('\n\n {:-^30} \n\n'.format(' TUPLA no FOR '))
# Sem posição
for comida in lanche:
    print(f'Eu vou comer {comida}')
# Com posição incluindo biblioteca
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
# Com posição sem biblioteca
'''
Mesmo resultado do FOR acima, porém mostra posição sem bibliotecas
for cont in range(0, len(lanche)):
    # Mostrando as strings das tuplas
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    # Mostrando os índices das tuplas
    print(cont)
'''
