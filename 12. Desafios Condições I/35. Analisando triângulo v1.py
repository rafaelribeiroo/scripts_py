# 35. Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
# Para se formar um triângulo, o primeiro segmento deve ser inferior a soma dos
# demais, e assim sucessivamente.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
