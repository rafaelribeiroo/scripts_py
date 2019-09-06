# 102. Crie uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e o outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :return: O valor do Fatorial de um número n.
    '''
    print('-' * 30)
    # Para exibir o número sendo subtraído a cada iteração
    c = n
    # Fator nulo de fatoração é 1, então se não fizer nenhum cálculo...
    multiplicação = 1
    for contador in range(n, 0, -1):
        if show is True:
            print(f'{contador}', end='')
            print(' x ' if c != 1 else ' = ', end='')
        multiplicação *= c
        c -= 1
    return multiplicação


print(fatorial(5, show=True))
