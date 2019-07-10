pessoas = {'nome': 'Rafael', 'sexo': 'M', 'idade': 25}

# Como no dict não há o ENUMERATE, podemos utilizar as características vistas
# anteriormente para repesentá-lo
for key, value in pessoas.items():
    print(f'O {key} é {value}')
