# 99. Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.

def maior(* valores):
    contador = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for núm in valores:
        print(núm, end=' ')
        if núm > maior:
            maior = núm
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
