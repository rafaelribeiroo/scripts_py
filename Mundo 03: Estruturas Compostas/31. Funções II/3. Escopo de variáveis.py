def teste():
    # Escopo local
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Escopo global
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')  # Da erro
