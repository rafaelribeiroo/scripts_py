# 48. Faça um programa que calcule a soma entre todos os números ímpares que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = valores = 0
# Contagem de todos os números ímpares de 1 a 500 (último valor não entra em
# range)
for contador in range(1, 501, 2):
    # Se algum número ímpar for múltiplo de três
    if contador % 3 == 0:
        # Conta mais um
        valores += 1  # Valores = Valores + 1
        # E soma
        soma += contador
print(f'A soma de todos os {valores} valores solicitados é {soma}')
