# 48. Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
valores = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        valores += 1  # Valores = Valores + 1
        soma += n  # Soma = Soma + 1
print('A soma de todos os {} valores solicitados é {}'.format(valores, soma))
