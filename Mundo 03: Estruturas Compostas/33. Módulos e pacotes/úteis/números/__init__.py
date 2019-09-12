'''
A modularização nos ajuda até certo ponto, porque se tivermos muitos métodos
ocupando esse arquivo, ficará difícil para compreender.
Pensando nisso, surgem os pacotes de módulos.
OBS: Cada pacote deve conter um __init__.py
'''
def fatorial(n):
    f = 1
    for contador in range(1, n+1):
        f *= contador
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3
