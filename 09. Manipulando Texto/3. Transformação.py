# Uma string é imútavel, a instrução a seguir não é válida
# frase[0] = 'J'
frase = 'Rafael Ribeiro'

# O replace por si só não altera, temos que atribuí-lo
print(frase.replace('Ribeiro', 'Pereira'))
# O IN é BOOLEANO, diferente do find que mostra a posição
print('Ribeiro' in frase)
# Caixa alta
print(frase.upper())
# Caixa baixa
print(frase.lower())
# 1º caractere em caixa alta
print(frase.capitalize())
# 1º caractere de cada palavra em caixa alta
print(frase.title())
# Remoção dos espaços vagos inúteis no início/fim (usuários leigos)
n = input('Digite seu nome: ')
print(n.strip())
# Muitas funções que tratam strings tem a variação R, que começa a tratar
# pela direita
print(n.rstrip())
# Começa pela esquerda
print(n.lstrip())
