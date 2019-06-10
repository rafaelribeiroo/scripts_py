início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
# Porque fim + 1?
# Como o PY sempre desconsidera o último valor (ao trabalhar com range),
# colocamos +1 para ficar mais 'readable by humans'
for contador in range(início, fim + 1, passo):
    print(contador)
print('FIM')
