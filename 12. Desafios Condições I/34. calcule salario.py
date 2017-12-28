#34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o seu salário? '))
if salario <= 1250:
    aumento = salario+(salario*15)/100
    print('O seu salário de R$ {:.2f} com o aumento de 15% será de R$ {:.2f}'.format(salario, aumento))
else:  
    aumento = salario+(salario*10)/100
    print('O seu salário de R$ {:.2f} com o aumento de 10% será de R$ {:.2f}'.format(salario, aumento))
