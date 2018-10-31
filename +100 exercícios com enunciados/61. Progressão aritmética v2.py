# 62. Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura
# while.

# Já fizemos o exercício no for anteriormente, mas não caia na
# falácia que for exige mais memória, for é mais rápido...
# Não caia nessa, pois não tem isso na programação, você faz
# o que achar melhor.
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
# No while não precisamos do fundamento matemático do exercício 51
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
