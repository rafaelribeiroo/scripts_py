# 108. Adapte o código do desafio 107, criando uma função adicional chamada
# moeda() que consiga mostrar os valores como um valor monetário formatado.

from stuff_107 import números

preço = float(input('Digite o preço: R$'))
print(f'Você digitou {números.moeda(preço)}')
