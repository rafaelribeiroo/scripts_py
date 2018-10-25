# 22. Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas
# > O nome com todas minúsculas
# > Quantas letras ao todo (sem considerar espaços)
# > Quantas letras tem o primeiro nome
n = str(input('Nome Completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(n.upper()))
print('Seu nome em minúsculas é {}'.format(n.lower()))
# Vai ser o comprimento total - a quantidade de vezes que aparece espaço, lembrando que os espaços iniciais e finais já foram removidos no strip
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
# O find localiza a 1ª vez que aparece o parâmetro informado
print('Seu 1º nome tem {} letras'.format(n.find(' ')))
# Outra forma:
# separa = n.split()
# print('Seu 1º nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
