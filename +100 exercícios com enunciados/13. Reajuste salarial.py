# 13. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento.

salário = float(input('Qual é o salário do funcionário? R$ '))
novo = salário + (salário * 15 / 100)
print(f'Um funcionário que ganhava R$ {salário:.2f}, com 15% de aumento, '
      f'passa a receber R${novo:.2f}')
