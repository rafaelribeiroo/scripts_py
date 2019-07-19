# 71. Crie um programa que simule o funcionamento de um caixa eletrônico. No
# início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format(' BANCO CEV '))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
montante = valor
# Cédula atual/Vamos começar com a maior e a medida que não puder mais entregar
# 50, vou entregando cédulas de menor valor.
cédula = 50
total_cédula = 0
# Não interrompa o laço enquanto meu montante não tiver zerado
while True:
    # Eu consigo tirar R$50 (atual/1º loop) do meu montante?
    if montante >= cédula:
        # Quantas vezes consigo pegar R$50 sob o total?
        montante -= cédula
        # Quantidade de vezes que tirei R$50
        total_cédula += 1
    else:
        # Validação para me exibir apenas as cédulas/quantidade cédular que
        # peguei, ocultando as cédulas que não precisei.
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de R${cédula}')
        # Sinal de que não consigo tirar mais R$50
        if cédula == 50:
            # Então converto minha cédula para R$20 pra ver se posso tirar
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if montante == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
