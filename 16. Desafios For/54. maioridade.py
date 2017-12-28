#54. Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
nascto = 0
maior = 0
menor = 0
for c in range(1, 2+1, 1):
    nascto = int(input('Qual o seu ano de nascimento? '))
    if atual - nascto < 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoa(s) não completaram a maioridade'.format(maior))
print('{} pessoa(s) JÁ completaram a maioridade'.format(menor))
