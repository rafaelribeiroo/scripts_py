# 50. Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar,
# desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(c)))
    if numero % 2 == 0:
        cont += 1
        soma += numero
if cont == 0:
    print('Você não informou nenhum número PAR, portanto a soma é 0')
elif cont == 1:
    print('Você informou apenas 1 número par: {}, portanto não tem como somar.'.format(soma))
else:
    print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
