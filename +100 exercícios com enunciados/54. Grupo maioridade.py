# 54. Crie um programa que leia o ano de nascimento de 7 pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas
# já são maiores.
from datetime import date

atual = date.today().year
menor, maior = 0, 0
for cont in range(1, 7 + 1, 1):
    nascto = int(input('Em que ano a {}ª pessoa nasceu? '.format(cont)))
    # Se a idade for maior ou igual a 21 ela já é de maior
    if atual - nascto >= 21:
        # Mesma coisa se eu fizesse maior = maior + 1
        maior += 1
    # Senão, de menor
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também, tivemos {} pessoas menores de idade'.format(menor))
