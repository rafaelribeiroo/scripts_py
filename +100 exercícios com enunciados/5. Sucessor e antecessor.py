# 5. Faça um programa que leia um número Inteiro e mostre
# na tela o seu sucessor e antecessor
n = int(input('Entre com um número: '))
# ant = n - 1
# suc = n + 1
# Porque dessa forma e não usar 3 variáveis?
# Quanto menos você utilizar variáveis, mais memória você vai economizar
# do seu dispositivo. Porém para deixar claro, não precisamos economizar
# memória, mais pra frente é mais recomendável usar variáveis porque
# se não dará muita dor de cabeça
print('Analisando o valor {},\n Seu antecessor é: {};\n E o sucessor: {}.'.format(n, (n - 1), (n + 1)))
