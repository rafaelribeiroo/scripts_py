# 62. Melhore o DESAFIO 061, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.
pt = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
tm = 1
dc = pt + (10) * rz
while pt < dc:
    print(pt, end=' ')
    pt = pt + rz
tm = int(input('\nQuer mostrar mais quantos termos?'))
dc = pt + (tm) * rz
