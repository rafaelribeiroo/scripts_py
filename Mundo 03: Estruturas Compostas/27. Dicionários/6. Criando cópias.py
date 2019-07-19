estado = dict()
brasil = list()
for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # [:] não funciona, então representamos com o copy()
    brasil.append(estado.copy())

# Itera informações do estado como um todo
for elemento in brasil:
    # Itera chaves e valores
    for key, value in elemento.items():
        print(value, end=' ')
    print()
