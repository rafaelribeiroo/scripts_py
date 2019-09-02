def contador(a=0, b=0, c=0):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    soma = a + b + c
    print(f'A soma vale {soma}')


# somar(3, 2)
somar()
# os parâmetros opcionais do print são: sep/end/flush/file
somar(3, 5, 8, 7)  # Dá erro, porque o esperado são 3, e estamos enviando 4
