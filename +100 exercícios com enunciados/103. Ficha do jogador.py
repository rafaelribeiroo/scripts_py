# 103. Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O
# programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))

# Se for numérico os gols
if g.isnumeric():
    # Não faça nada, já que ele já será numérico
    g = int(g)
# Se não for numérico
else:
    # Agregamos um valor nulo
    g = 0
# Se não tiver nada no nome
if n.strip() == '':
    # Passe apenas a quantidade de gol
    ficha(gol=g)
else:
    # Se tiver, passe o nome recebido e qntde de gols
    ficha(n, g)
