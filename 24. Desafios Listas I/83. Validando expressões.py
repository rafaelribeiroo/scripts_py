# 83. Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.
pa = re = 0
e = str(input('Digite a expressão: '))
for caracter in e:
    if '(' in caracter:
        pa += 1
    elif ')' in caracter:
        re += 1
if pa == re:
    print('A expressão está correta')
elif pa > re:
    print('A expressão está incorreta, feche o parênteses')
else:
    print('A expressão está incorreta, abre o parênteses')
