# 7. Desenvolva um programa que leia as duas notas de um aluno, calcule e
# mostre a sua média

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
# Quando insiro 1 casa após o ponto o PY aplica as regras algébricas de
# arredondamento
print(f'Sua média foi: {média:.1f}')
