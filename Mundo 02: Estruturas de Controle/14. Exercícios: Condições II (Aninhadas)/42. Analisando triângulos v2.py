# 42. Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# > Equilátero: Todos os lados iguais
# > Isósceles: Dois lados iguais
# > Escaleno: Todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro segmento: '))
# Para se ter um triângulo, cada lado deve ser inferior a soma dos outros 2
# lados
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    # Pra comparar a semelhança/congruência entre todas variáveis
    # o PY permite a condição abaixo
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        '''
        se fôssemos fazer como acima (r1 == r2 == r3), na hora de identificar o
        ISÓSCELES ele identificaria EQUILÁTERO. Já que para assemelhar os 3 eu
        posso afirmar que todos são iguais/Já ao contrário, a reta 1 deve ser
        diferente da 2, assim como a 2 deve ser diferente da 3. Então como
        saberia se a 1 é diferente da 3?
        '''
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
