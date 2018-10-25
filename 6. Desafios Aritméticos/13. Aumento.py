# 13. Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: '))
qntde_aumento = int(input('Entre com a porcentagem de aumento: '))
aumento = salario + (salario * qntde_aumento / 100)
print('*' * 10)
print('Seu salário atual é: {:.2f}'.format(salario), end=', ')
print('mas, com o acréscimo de {}%'.format(qntde_aumento), end=', ')
print('vai para {:.2f}!'.format(aumento))
