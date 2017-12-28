valor = float(input('Qual o valor da sua viagem? '))
distancia = float(input('Qual a distância até o destino em km/h: '))
calculaKm = valor/distancia
if calculaKm < 1:
    print('Por cada km rodado você pagará R$ {:.2f} centavos'.format(calculaKm))
else:
    print('Por cada km rodado você pagará R$ {:.2f} reais'.format(calculaKm))
