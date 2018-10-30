# 56. Desenvolva um programa que leia o nome, idade e sexo de
# 4 pessoas. No final do programa, mostre:
# > A média de idade do grupo.
# > Qual é o nome do homem mais velho.
# > Quantas mulheres têm menos de 20 anos.
soma_idade, médiaidade, maioridadehomem, totmulher20 = 0, 0, 0, 0
nomevelho = ''
for p in range(1, 4 + 1, 1):
    print('-' * 5, '{}ª PESSOA'.format(p), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()
    # Recolhendo todas as idades e somando
    soma_idade += idade
    # Se for a primeira pessoa a mais velha, e se M for o sexo
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    # Se o mais velho estiver depois do 1º
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    # Se for mulher e tiver menos de 20 anos
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
# Para se obter uma média de idade, precisamos de todas
# as idades somadas dividido pela quantidade de pessoas
médiaidade = soma_idade / 4
print('A média de idade do grupo é de {:.2f} anos'.format(médiaidade))
print('O homem mais velho tem ' +
      '{} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
