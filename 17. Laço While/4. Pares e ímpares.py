n = 1
par = impar = 0
# Enquanto n for diferente de 0, faça:
while n != 0:
    n = int(input('Digite um valor: '))
    # O 0 é só para saída do programa, o IF é para
    # não contar ele.
    if n != 0:
        # Se o resto da divisão por 2 for igual a 0, PAR
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
