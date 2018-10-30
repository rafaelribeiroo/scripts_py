r = 'S'
# Percebe a grande diferença? No while podemos criar situações
# onde façamos laços indeterminadamente, não tenho que determinar
# um range (Faça isso 10x, 20x/)

# Exemplo prático, leia o nome de todas as pessoas que chegarem
# ao meu estabelecimento, mas não sei quantas são.
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
