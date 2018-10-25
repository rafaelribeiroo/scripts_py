# 7. Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média
nota1 = float(input('Digite Sua 1ª nota: '))
nota2 = float(input('2ª nota: '))
# m = (nota1 + nota2) / 2
# Regras Algébricas de Arredondamento quando insiro 1 casa após o ponto
print('Sua média foi: {:.1f}'.format((nota1 + nota2) / 2))
