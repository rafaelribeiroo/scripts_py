# No PY, todos os comandos fornecem uma documentação para melhor compreensão,
# que pode ser acessada através de help(método). Em nossas funções, é
# possível oferecer isso também através dos comentários abaixo.


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2, 10, 2)
# A partir disso, basta dar um help(contador)
