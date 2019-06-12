# 14. Escreva um programa que converta uma temperatura digitada em ºC e
# converta para ºF.

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = 9 * celsius / 5 + 32
kelvin = celsius + 273.15
print(f'A temperatura de {celsius}ºC corresponde a {fahrenheit}ºF e '
      f'{kelvin}ºK')
