# 50. Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar,
# desconsidere-o.

soma = contador_pares = 0
for contador_for in range(1, 7):
    número = int(input(f'Digite o {contador_for}º valor: '))
    if número % 2 == 0:
        contador_pares += 1
        soma += número
if contador_pares == 0:
    print('Você não informou nenhum número PAR, portanto não há soma')
elif contador_pares == 1:
    print(f'Você informou apenas 1 número par {soma}')
else:
    print(f'Você informou {contador_pares} números PARES e a soma foi {soma}')
