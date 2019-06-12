galera = list()
dado = list()

# Posso atribuir o valor de uma variável a outra caso simples/não compostas
totalmaior = totalmenor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    # O Clear limpa a estrutura
    dado.clear()

# Análise pra ver se é maior de idade
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')
