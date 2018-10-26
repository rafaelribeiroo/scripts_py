# 40. Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 6.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m < 5.0:
    print('REPROVADO!')
elif 7 > m >= 5:  # OR elif m <= 5 or m < 7 mas o PY aceita esse jeito também
    print('RECUPERAÇÃO!')
elif m > 7:
    print('APROVADO!')
