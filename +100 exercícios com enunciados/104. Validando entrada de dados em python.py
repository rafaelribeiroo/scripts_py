# 104. Crie um programa que tenha a função leiaInt(), que vai funcionar de
# forma semelhante à função input() do Python, só que fazendo a validação
# para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')


def leiaInt(msg):
    # VAR booleana para validarmos
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        # Se for numérico, não faremos nada
        if n.isnumeric():
            # A não ser declarar o óbvio e sair do loop
            valor = int(n)
            ok = True
        # Caso contrário, descreva um valor
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
