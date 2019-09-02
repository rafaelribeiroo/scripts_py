def somar(a=0, b=0, c=0):
    s = a + b + c
    # print('A soma vale {s}')
    # Útil para personalização de resultados
    return s


# somar(3, 2, 5)
# somar(2, 2)
# somar(6)
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')
