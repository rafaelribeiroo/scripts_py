#35. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('1ª Segmento: '))
r2 = float(input('2ª Segmento: '))
r3 = float(input('3ª Segmento: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('É um triângulo!')
else:
    print('Não é!')
