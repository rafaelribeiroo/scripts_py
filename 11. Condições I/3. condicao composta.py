n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('2ª nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns pela nota!' if m >= 6 else 'Estude mais!')
'''if m >= 6:
    print('Sua média foi boa, PARABÉNS')
else:
    print('Você deveria estudar mais!')'''
