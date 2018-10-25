i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
# Porque f+1? Como o Py sempre desconsidera o último valor informado colocamos +1 para ser mais 'readable by humans'
for c in range(i, f + 1, p):
    print(c)
print('FIM')
