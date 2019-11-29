def teste(b):
    # Nova variável, já que a outra é global.
    # a = 8
    # Para tratarmos a var: "a" global:
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
# Da erro por falta de escopo
print(f'B dentro vale {b}')
print(f'C dentro vale {c}')
