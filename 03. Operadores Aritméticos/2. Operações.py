n1 = int(input('1º valor: '))
n2 = int(input('2º: '))

# Somar
s = n1 + n2
# Subtrair
sub = n1 - n2
# Multiplicar
m = n1 * n2
# Dividir
d = n1 / n2
# Resto da Divisão
di = n1 // n2
# Exponenciação
e = n1 ** n2
# Potência
p = pow(n1, n2)  # 4 elevado ao cubo (se o 2 for 3)
# Raíz quadrada
rq = n1 ** (1 / 2)
# Raíz cúbica
rc = n1 ** (1 / 3)

# :.<número>f é para filtrar quantos num após a casa eu exibirei
print(f'A soma é {s}; \nO produto é {m}; \nDivisão é {d:.3f}', end=' → ')
# O end serve para deixar dois print na mesma linha
print('Divisão inteira é {} e a potência: {}'.format(di, e))
