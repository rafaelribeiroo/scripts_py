# 40. Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# > Média abaixo de 5.0: REPROVADO
# > Média entre 6.0 e 6.9: RECUPERAÇÃO
# > Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}')
# if média >= 5 and média < 7
if 7 > média >= 5:
    # Para compreensão acima, à direita não muda, à esquerda devemos redigir o
    # sinal ao contrário, no caso, < 7. Muito parecido com a matemática
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
