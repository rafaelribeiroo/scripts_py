print('Qual é o preço?')
p = float(input('R$ '))
print('Qual é o preço após o desconto?')
np = float(input('R$ '))
d = 100-(np*100/p)
print('Seu preço reduziu {:.0f}%'.format(d))
if d>=20:
   print('> É um bom desconto')
else:
   print('> É um desconto relativamente ruim')
