# 85. Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente
p = list()
i = list()
total = list()

for contador in range(1, 7 + 1):
    num = int(input(f'Digite o {contador}° valor: '))
    if num % 2 == 0:
        p.append(num)
    else:
        i.append(num)
total.append(p)
total.append(i)
print(sorted(total))
