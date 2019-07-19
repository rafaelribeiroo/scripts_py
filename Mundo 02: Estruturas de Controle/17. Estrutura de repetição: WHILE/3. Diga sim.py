resposta = 'S'
# Percebe a grande diferença? No while podemos criar situações onde façamos
# laços indeterminadamente, não tenho que determinar um range (Faça isso
# 10x, 20x)

# Leia o nome de todas as pessoas que chegarem ao meu estabelecimento, não sei
# quantas virão
while resposta == 'S':
    nome = str(input('Informe o nome: '))
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim')
