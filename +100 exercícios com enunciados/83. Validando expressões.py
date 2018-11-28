# 83. Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.
expressão = str(input('Digite a expressão: '))
pilha = []
for símbolo in expressão:
    # Se houver um parentêses aberto
    if símbolo == '(':
        # Inclui na minha pilha
        pilha.append('(')
    # Se houver um parentêses fechado
    elif símbolo == ')':
        # Conferimos se a pilha tem algum aberto
        if len(pilha) > 0:
            # Se houver, pode remover o aberto, já que
            # foi fechado
            pilha.pop()
        else:
            # Se for igual a 0, inclui um fechando
            pilha.append(')')
            break
# Se não houver nenhum parênteses na pilha, tá OK
if len(pilha) == 0:
    print('Sua expressão está válida!')
# Se ainda houver, tá errada
else:
    print('Sua expressão está errada!')

        
