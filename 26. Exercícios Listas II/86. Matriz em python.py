matriz = [[], [], []]
for cont1 in range(1, 3 + 1):
    matriz[0].append(
        int(input(f'Digite um valor para [0][{cont1}]: '))
    )
for cont2 in range(1, 3 + 1):
    matriz[1].append(
        int(input(f'Digite um valor para [1][{cont2}]: '))
    )
for cont3 in range(1, 3 + 1):
    matriz[2].append(
        int(input(f'Digite um valor para [2][{cont3}]: '))
    )
print('-=' * 30)
print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]')
