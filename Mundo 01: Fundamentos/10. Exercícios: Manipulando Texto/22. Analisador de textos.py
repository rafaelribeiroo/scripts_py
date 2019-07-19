# 22. Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas
# > O nome com todas minúsculas
# > Quantas letras ao todo (sem considerar espaços)
# > Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
# Comprimento total subtraído Espaços em branco
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
# Pedindo pra localizar um espaço vazio da esquerda pra direita, saberemos
# quantos caracteres existem no primeiro nome.
print(f"Seu 1º nome tem {nome.find(' ')} letras")
