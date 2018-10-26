# 51. Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
# Vai começar do número que você decidiu
# Pulando de quantos em quantos você informou
# Décimo + Razão porque se não o PY ia somente até o penúltimo loop
for c in range(primeiro, décimo + razão, razão):
    print(c, end=' →')
print('ACABOU')
