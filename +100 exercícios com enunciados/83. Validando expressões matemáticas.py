# 83. Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

expressão = str(input('Digite a expressão: '))
pilha = list()
for símbolo in expressão:
    # Se houver um parentêses aberto
    if símbolo == '(':
        # Atribui a minha pilha
        pilha.append('(')
    # Se houver um parentêses fechado
    elif símbolo == ')':
        # Conferimos se a pilha tem algum aberto
        if len(pilha) > 0:
            # Se houver, pode remover o aberto, já que
            # foi fechado
            pilha.pop()
        # Caso a pilha estiver vazia, é sinal que tem mais sinal fechando que
        # abrindo, o que vai causar erro mais abaixo
        else:
            # Inclui outro fechamento, para ocasionar erro
            pilha.append(')')
            break
# Se o tamanho da pilha for 0, quer dizer que todo parêntesis que foi aberto,
# foi encerrado
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
