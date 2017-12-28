#15. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
aluguel = int(input('Por quantos dias o automóvel foi alugado? '))
kmsRodados = float(input("Quantos km's rodados? "))
valor = (aluguel*60) + (kmsRodados*0.15)
print('O valor do aluguel será de R${:.2f}'.format(valor))
#Dica: Se o enunciado for muito grande, modularize seu código, faça por partes.
#Dividir pra Conquistar
