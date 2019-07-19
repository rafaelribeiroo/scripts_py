pessoas = {'nome': 'Rafael', 'idade': 25}

# Dict não possui append, mas podemos inserir
pessoas['sexo'] = 'M'

# Alteração de valores
pessoas['nome'] = 'Gabriel'

# Remoção de elementos
del pessoas['idade']

print(f'{pessoas}')
