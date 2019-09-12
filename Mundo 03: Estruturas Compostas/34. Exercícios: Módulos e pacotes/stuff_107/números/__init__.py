def moeda(moeda):
    return f'{moeda:.2f}'.replace('.', ',')


def metade(moeda):
    moeda /= 2
    return moeda


def dobro(moeda):
    moeda *= 2
    return moeda


def aumentar(moeda, desconto=10):
    moeda += (moeda * desconto) / 100
    return moeda


def diminuir(moeda, desconto=13):
    moeda -= (moeda * desconto) / 100
    return moeda
