# Faça um programa que mostre a tabuada de vários números, um de cada vez, para
# cada valor digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.

while True:
    núm = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if núm < 0:
        print('Não realizamos tabuadas de números negativos')
        break
    for c in range(1, 10 + 1):
        print(f'{núm} x {c:2} = {núm*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
