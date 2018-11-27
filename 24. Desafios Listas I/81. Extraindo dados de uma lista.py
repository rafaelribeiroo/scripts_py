# 81. Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# > Quantos números foram digitados
# > A lista de valores, ordenada de forma decrescente
# > Se o valor 5 foi digitado e está ou não na lista.
lista = list()
resp = ' '
c = 0
while resp not in 'N':
    lista.append(int(input('Digite um valor: ')))
    c += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
lista.sort(reverse=True)
print(f'Você digitou {c} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
print(f'O valor 5 faz parte da lista' if 5 in lista
      else 'O valor 5 NÃO faz parte da lista')
