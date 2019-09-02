# 102. Crie uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e o outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(num, show):
    if show == True:
        num = 1
        for contador in range(num, 0, -1):
            num *= contador
            print(f'{contador} ', end='x')
        return num


n = int(int('Fatorial: '))
fatorial(n, show=True)
