#2. Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome = str(input('Qual o seu nome? '))
dia = int(input('Qual o dia do seu aniversário {}? '.format(nome)))
mês = str(input('E o mês? '))
ano = int(input('Do ano: '))
print(f'Você faz aniversário no dia {dia} de {mês} de {ano}, é um prazer {nome}')