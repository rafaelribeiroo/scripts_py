# 29. Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.
km = float(input('Qual a velocidade atual do carro? '))
if km > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    m = (km - 80) * 70
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
else:
    print('Tenha um bom dia! Dirija com segurança!')
# Ou posso retirar do else e deixar sem condições, terá o mesmo resultado
