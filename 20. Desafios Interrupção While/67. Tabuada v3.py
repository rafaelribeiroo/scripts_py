# Faça um programa que mostre a tabuada de vários números, um de cada vez, para
# cada valor digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.
núm = 1
while True:
    núm = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 25)
    if núm < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    for c in range(0, 10 + 1):
        print(f'{núm} x {c:>2} = {núm * c}')
    print('-' * 25)
