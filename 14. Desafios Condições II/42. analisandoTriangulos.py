#42. Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: Todos os lados iguais
#- Isósceles: Dois lados iguais
#- Escaleno: Todos os lados diferentes
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    #Pra comparar se todos forem semelhantes, congruents o PY permite a condição abaixo
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    #Na diferença se fossemos fazer como acima daria erro, que na hora de colocar ISÓSCELES ele falaria que é EQUILÁTERO, porque se for pra comparar semelhança entre os 3 eu posso afirmar que reta 1 é igual reta 3, já na diferença reta 1 é diferente de 2, reta 2 é diferente de reta 3, como saberei se reta 1 é diferente de reta 3?
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else: 
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
