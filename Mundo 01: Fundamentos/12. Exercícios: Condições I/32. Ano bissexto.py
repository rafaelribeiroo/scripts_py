# 32. Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Que ano quer analisar? 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
# Para descobrir se um ano é BISSEXTO, precisamos seguir 3 dicas cruciais
# > Se o ano for divisível com 4, o resto dará 0
# > Se o ano for divisível com 100, não pode ser diferente de 0
# > Se o ano for divisível com 400, o resto dará 0
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
