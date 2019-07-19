# 51. Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
# final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
# Fórmula para calcular o décimo (enésimo) termo de uma PA
décimo = primeiro + (10 - 1) * razão

# O for começa do número que você decidiu (primeiro) pulando de quantos em
# quantos você informou (razão) e vai até o DÉCIMO + RAZÃO porque se não o
# PY ia somente até o penúltimo loop
for contador in range(primeiro, décimo + razão, razão):
    print(contador, end=' → ')
print('ACABOU')
