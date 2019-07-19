# 86. Crie um programa que crie uma matriz de dimensão 3x3 e preencha com
# valores lidos pelo teclado.
'''
   _____
0 |_|_|_|
1 |_|_|_|
2 |_|_|_|
   0 1 2
'''
# No final, mostre a matriz na tela, com a formatação correta.

# Definimos o esqueleto com os "0" para não ter que usar o append
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# For de alimentação
for linha in range(0, 3):
    # Enquanto não percorrer do 0 ao 2, não passa pra segunda iteração, de
    # 0 pra 1 no caso
    for coluna in range(0, 3):
        # Insere na posição correta
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: ')
        )
print('-=' * 30)
# For de exibição
for linha in range(0, 3):
    for coluna in range(0, 3):
        # Colocamos o abrangente para ficar melhor identado
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
