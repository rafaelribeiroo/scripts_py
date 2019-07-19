# 31. Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
# e R$0,45 para viagens mais longas.

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km/h.'.format(distância))
# PY não possui operador ternário
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua viagem será de R${preço:.2f}')
