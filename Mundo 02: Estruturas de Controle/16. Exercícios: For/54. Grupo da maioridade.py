# 54. Crie um programa que leia o ano de nascimento de 7 pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

from datetime import date

atual = date.today().year
total_menor = total_maior = 0
for contador in range(1, 7 + 1, 1):
    nascimento = int(input(f'Em que ano a {contador}ª pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 21:
        total_maior += 1
    # Senão, de menor
    else:
        total_menor += 1
print(f'Ao todo tivemos {total_maior} pessoas maiores de idade')
print(f'E também, tivemos {total_menor} pessoas menores de idade')
