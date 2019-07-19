# Precisamos atribuir qualquer valor aqui que seja diferente de 0, porque na
# chamada do while, definimos que enquanto for diferente de 0, vai rodar.
n = 1
par = ímpar = 0

# Enquanto n for diferente de 0, faça:
while n != 0:
    n = int(input('Digite um valor: '))
    # Se for zero, saia do loop. Se for válido...
    if n != 0:
        # Resto da divisão é igual a 0? Então temos um número par
        if n % 2 == 0:
            par += 1
        # É igual a 1? Número ímpar
        else:
            ímpar += 1
print('Contamos {} números pares e {} ímpares'.format(par, ímpar))
