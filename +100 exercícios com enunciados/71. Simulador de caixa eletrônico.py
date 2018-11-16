# 71. Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 30)
print('{:^30}'.format(' BANCO CEV '))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
# Montante/total
total = valor
céd = 50
totcéd = 0
# Não pare o laço enquanto eu não contar todas as notas que vou entregar
# ao usuário
while True:
    # Se o montante for maior ou igual 50
    if total >= céd:
        # Vai remover do total 50 reais
        total -= céd
        # E contar como 1 cédula a ser entregue
        totcéd += 1
    # Caso contrário, não for igual a 50, 80 no caso
    else:
        # Não printe nada se ele não quiser pegar nem 1 real
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        # Se o montante tiver 50/100/150, remova do total
        if céd == 50:
            céd = 20
        # E assim sucessivamente
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
