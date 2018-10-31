# 8. Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros
# Unidades de medida
metros = float(input('Uma distância em metros: '))
print('A medida de: {}m corresponde(m) a'.format(metros))
print('{}km'.format(metros / 1000))  # 1000m equivalem a 1 quilômetro
print('{}hm'.format(metros / 100))  # 100m  equivalem a 1 hectómetro
print('{}dam'.format(metros / 10))  # 10m   equivalem a 1 decâmetro
print('{:.0f}dm'.format(metros * 10))  # 10   decímetros equivalem a 1m
print('{:.0f}cm'.format(metros * 100))  # 100  centímetros equivalem a 1m
print('{:.0f}mm'.format(metros * 1000))  # 1000 milímetros equivalem a 1m
