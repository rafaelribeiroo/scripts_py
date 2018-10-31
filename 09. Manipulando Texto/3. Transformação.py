# Informação Importante antes de começar:
# Uma string é imútavel, então não posso usar:
# frase[0] = 'J'
# O replace por si só não altera.
# Temos que atribui-lo a alguma variável para isso
frase = 'Curso em Video Python'
# Substituir o 1º parâmetro pelo 2º
print(frase.replace('Python', 'Android'))
# Diferente do find que mostra a posição visto anteriormente.
# Aqui retornará True or False
print('Curso' in frase)
# Caixa alta
print(frase.upper())
# Caixa baixa
print(frase.lower())
# Apenas o primeiro caractere de cada frase em maiúsculo
print(frase.capitalize())
# Todo primeiro caractere de frase em maiúsculo
print(frase.title())
# Geralmente, há casos de usuários que ao preencherem um formulário, já no
# primeiro input pressionam a barra de espaços algumas vezes pra ver se tá
# "funcionando", com base nesses casos algumas linguagens têm a opção de
# eliminar esses espaços vagos no início (e fim), para deixar apenas o
# essencial.
n = input('Digite seu nome: ')
print(n.strip())
# Muitas funções dentro do python que tratam strings tem a variação R, que
# começa a tratar pela direita
print(n.rstrip())
# Pela esquerda
print(n.lstrip())
