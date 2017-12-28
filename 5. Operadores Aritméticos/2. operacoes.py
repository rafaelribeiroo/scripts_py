n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
#print('A soma vale {}'.format(n1+n2))
#Subtração
#r = n1 -n2
#Soma
s = n1 + n2
#Multiplicar
m = n1 * n2
#Dividir
d = n1 / n2
#Resto da Divisão, 2/5 é 3 certo? Mas o que sobra (pra continuar operação?), sobra 0
di = n1 // n2
#Exponenciação
e = n1 ** n2
#Separando os pontos flutuantes com . e apresentando 3 após a casa, FLUTUANTES
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' >>> ') # o end serve para deixar 2 prints na mesma linha
print('Divisão inteira {} e potência {}'.format(di, e))

