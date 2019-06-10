nome = input('Qual é seu nome? ')
# :20 abrange 20 espaços vagos (nunca slice)
# = completa os espaços vagos com igual

# ^ centraliza o dado da var
print('Prazer em te conhecer {:=^20}!'.format(nome))
# > Alinha a direita
print('Prazer em te conhecer {:>20}!'.format(nome))
# < Alinha a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
