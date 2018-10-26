# 31. Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até
# 200km e R$0,45 para viagens mais longas.
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km/h.'.format(distancia))
# O python não possui operador ternário
preco = distancia * 0.50 if distancia <= 200 else distancia * .045
print('O valor da sua viagem será de R${:.2f}'.format(preco))
