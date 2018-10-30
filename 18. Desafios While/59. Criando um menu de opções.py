# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

opcao = maior = 0
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    print('=-=' * 10)
    sleep(1)
    if opcao == 1:
        soma = pv + sv
        print('A soma entre {} + {} é {}'.format(pv, sv, soma))
    elif opcao == 2:
        multiplicar = pv * sv
        print('O resultado de {} x {} é {}'.format(pv, sv, multiplicar))
    elif opcao == 3:
        if pv > sv:
            print('Entre {} e {} o maior valor é {}'.format(pv, sv, pv))
        else:
            print('Entre {} e {} o maior valor é {}'.format(sv, pv, sv))
    elif opcao == 4:
        print('Informe os números novamente:')
        pv = int(input('Primeiro valor: '))
        sv = int(input('Segundo valor: '))
    elif opcao > 5:
        print('Opção inválida!!')
    print('Finalizando')

