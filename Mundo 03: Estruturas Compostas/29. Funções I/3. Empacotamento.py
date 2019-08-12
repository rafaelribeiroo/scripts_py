# A maioria das linguagens de programação não aceitam isso, mas o PY sim!

# Eu recebo vários números, quantos? Não sei, se vira aí.
def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')

def quantidade(* núm):
    tamanho = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tamanho} números')

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(8, 0)
quantidade(5, 7, 3, 1, 4)
quantidade(8, 4, 7)
quantidade(8, 0)
