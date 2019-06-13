# 81. Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# > Quantos números foram digitados
# > A lista de valores, ordenada de forma decrescente
# > Se o valor 5 foi digitado e está ou não na lista.

valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

print('-=' * 20)
# Tamanho da minha lista
print(f'Você digitou {len(valores)} elementos.')
# Lista em ordem decrescente
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
# Condição para verificar existência do 5
if 5 in valores:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
