# 98. Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: início, fim e passo e realize a contagem. Seu programa tem que
# realizar três contagens através da função criada:
# > De 1 até 10, de 1 em 1
# > De 10 até 0, de 2 em 2
# > Uma contagem personalizada.

from time import sleep


def contador(i, f, p):
    # Se o passo for negativo eu vou
    if p < 0:
        # Trocar pra positivo
        p *= -1
    if p == 0:
        p = 1
    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        contador = i
        # Enquanto o contador for menor ou = (pra parar exatamento no 10), não
        # finalize
        while contador <= f:
            # Nas últimas versões do PY, ele cria um buffer de tela (aguarda
            # todas as iterações que têm um sleep carregarem para exibir)
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador += p
        print('FIM!')
    else:
        contador = i
        # Se o fim for menor que o início, vamos "negativar" o passo para
        # retrocesso
        while contador >= f:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador -= p
        print('FIM!')
    print('-' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
