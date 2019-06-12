# 8. Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros

metros = float(input('Uma distância em metros: '))
print(f'A medida de {metros}m corresponde(m) a')
print(f'{metros/1000}km')  # 1000m equivalem a 1 quilômetro
print(f'{metros/100}hm')  # 100m equivalem a 1 hectómetro
print(f'{metros/10}dam')  # 10m equivalem a 1 decâmetro
print(f'{metros*10:.0f}dm')  # 10 decímetros equivalem a 1m
print(f'{metros*100:.0f}cm')  # 100 centímetros equivalem a 1m
print(f'{metros*1000:.0f}mm')  # 1000 milímetros equivalem a 1m
