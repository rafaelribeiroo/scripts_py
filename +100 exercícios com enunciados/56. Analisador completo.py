# 56. Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No
# final do programa, mostre:
# > A média de idade do grupo.
# > Qual é o nome do homem mais velho.
# > Quantas mulheres têm menos de 20 anos.

somatório_idade = média_idade = maior_idade_masculina = mulheres_menos_20 = 0
nome_mais_velho = ''
for pessoa in range(1, 4 + 1, 1):
    print('-' * 5, f'{pessoa}ª PESSOA', '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()[0]

    # Para saber a média de idade do grupo, preciso saber o total antes
    somatório_idade += idade
    # Se for a primeira pessoa a mais velha
    if pessoa == 1 and sexo in 'M':
        # Para obtermos o nome do mais velho, precisamos saber a idade antes
        maior_idade_masculina = idade
        nome_mais_velho = nome
    # Se o mais velho estiver depois do 1º
    if sexo in 'M' and idade > maior_idade_masculina:
        maior_idade_masculina = idade
        nome_mais_velho = nome
    # Se for mulher e tiver menos de 20 anos
    if sexo in 'F' and idade < 20:
        mulheres_menos_20 += 1

# Para obtermos a média, precisamos somar todas as idades e dividir pela qntde
# de pessoas cadastradas
média_idade = somatório_idade / 4
print(f'A média de idade do grupo é de {média_idade:.2f} anos')
print(f'O homem mais velho tem {maior_idade_masculina} anos e se chama '
      f'{nome_mais_velho}')
print(f'Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos')
