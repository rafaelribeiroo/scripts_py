# Por incrível que pareça, o PY aconselha a utilizar o import como
# import úteis, já que podemos ter dois métodos de dois módulos
# congruentes.
from úteis import números
# Sempre que ele realiza a importação, é gerado um __pycache__

# Quando temos muitas funções, códigos ocupando um mesmo arquivo, fica
# agradável modularizar.
num = int(input('Digite um valor: '))
fat = números.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {números.dobro(num)}.')
