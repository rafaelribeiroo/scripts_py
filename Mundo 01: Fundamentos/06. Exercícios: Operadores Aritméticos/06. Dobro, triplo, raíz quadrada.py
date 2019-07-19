# 6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz
# quadrada.

n = int(input('Digite um número: '))

# Porque entre parêntesis? Ordem de Precedência
print(f'O dobro de {n} vale {n*2}')
print(f'O triplo de {n} vale {n*3}')
print(f'A raíz quadrada de {n} é igual a {pow(n, (1/2)):.2f}')
