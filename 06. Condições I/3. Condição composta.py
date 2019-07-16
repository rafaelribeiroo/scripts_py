n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('2ª: '))
média = (n1 + n2) / 2
print(f'A sua média foi {média:.1f}')
# Condição composta encurtada
print('Parabéns pela nota!' if média >= 6 else 'Estude mais!')
