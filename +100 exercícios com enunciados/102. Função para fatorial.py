# 102. Crie uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e o outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    '''
    # Fator nulo de fatoração é 1
    fatorial = 1
    for contador in range(n, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(f'{contador} x ', end='')
            else:
                print(f' = ', end='')
        fatorial *= contador
    return fatorial


print(fatorial(5, show=True))
