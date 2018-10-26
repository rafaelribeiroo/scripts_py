nome = input('Qual é seu nome? ')
# Dentro das chaves:
# :20 serve para abranger 20 espaços vagos (nunca slice)
# = completar os espaços vagos com esse caractere, fora a var
# ^ centraliza a var no meio dos =
print('Prazer em te conhecer {:=^20}!'.format(nome))
# Abaixo desloco meu nome ao final da linha, direita
print('Prazer em te conhecer {:>20}!'.format(nome))
# Abaixo movo meu nome pro começo da linha, esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
