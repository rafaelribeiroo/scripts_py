# 42. Refaça o desafio 035 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    # Pra comparar se todos forem semelhantes, congruentes;
    # o PY permite a condição abaixo:
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    # Para analisar as demais possibilidades, Se fôssemos fazer como
    # acima daria erro, porque na hora de identificar ISÓSCELES
    # ele identificaria EQUILÁTERO; Já que para assemelhar os 3 eu
    # posso afirmar que todos serão iguais; Já ao contrário, a reta 1
    # deve ser diferente da 2, assim como a 2 deve ser diferente da 3.
    # Então como saberia se a 1 é diferente da 3?
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
