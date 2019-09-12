# 107. Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa
# que importe esse módulo e use algumas dessas funções.

from stuff_107 import números

preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é {números.metade(preço)}')
print(f'O dobro de {preço} é {números.dobro(preço)}')
print(f'Aumentando 10%, temos {números.aumentar(preço, 10)}')
print(f'Reduzindo 13%, temos {números.diminuir(preço, 13)}')
