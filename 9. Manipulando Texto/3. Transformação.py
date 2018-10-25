frase = 'Curso em Video Python'
# Substituir o 1º parâmetro pelo 2º, Python por Android no caso
# Lembrando que uma string é imútavel, então não posso usar:
# frase[0] = 'J'
# O replace por si so, nao altera a palavra, temos que atribui-lo
# a alguma variavel para isso
print(frase.replace('Python', 'Android'))
# Diferente do find, no find ele retornará a posição, aqui
# retornará True or False
# Mas, e se curso estivesse em lower case?
#     print(frase.lower().find('curso'))
print('Curso' in frase)
# Caixa alta
print(frase.upper())
# Caixa baixa
print(frase.lower())
# Apenas o primeiro caractere de cada frase em maiusculo
print(frase.capitalize())
# Todo primeiro caractere de frase em maiusculo
print(frase.title())

# Nossos pais têm o hábito de ao preencher algum formulário ele não clica no
# input e começa a digitar, ele clica aperta a barra de espaço algumas x pra
# ver se funciona e assim começa a escrever, isso tem se tornado normal e
# algumas linguagens tem a opção de eliminar esses espaços vagos no início e
# fim pra deixar apenas o essencial
n = input('Digite seu nome: ')
# O strip elimina os espaços vagos inúteis no início e fim
print(n.strip())
# Muitas funcoes dentro do python que tratam strings tem a variação R, que
# começa a tratar pela direita
print(n.rstrip())
# Pela esquerda
print(n.lstrip())
