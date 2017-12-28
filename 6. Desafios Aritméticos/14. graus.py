#14. Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
celsius = float(input('Informe a temperatura em ºC: '))
print('A temperatura de {}ºC corresponde a {}ºF!'.format(celsius, (celsius*1.8+32)), end=' e ')
print('{}ºK'.format(celsius+273.15))
