#6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
# d = n * 2
# t = n * 3
# rq = n**(1/2)
# Porque entre parêntesis? Ordem de Precedência
print('O dobro de {} vale {}'.format(n, (n * 2)), end=' & ')
# format é o método do objeto print
print('O triplo vale {}; \nEnfim, a raiz quadrada de {} é igual a {:.2f}'.format((n * 3), n, pow(n, (1 / 2))))
# Ou pode ser: n**(1/2)
