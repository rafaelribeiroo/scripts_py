# 47. Crie um programa que mostre na tela todos os números pares que estão
# no intervalo entre 1 e 50.
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou!')
# Outra forma: Caso o resto da divisão por 2 seja 0, printa meu número
# O grande problema disso é que ele fará muitas repetições, o que gera mais
# carga em meu processador.
