#11. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
#Obs: Cada m² preciso de 2 latas
print('*' * 20)
print('Informe a Alt. e Larg. em m² para saber quantas latas de tinta comprar')
print('*' * 20)
largura = float(input('Largura: '))
altura = float(input('Altura: '))
print('O total da área é de {}m²'.format(largura*altura))
print('Serão necessárias {:.0f} latas de tinta'.format((largura*altura)//2))
