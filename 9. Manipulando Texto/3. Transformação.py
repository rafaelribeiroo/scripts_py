frase = 'Curso em Video Python'
# Substituir o 1º parâmetro pelo 2º, Python por Android no caso
# Lembrando que uma string é imútavel, então não posso usar:
# frase[0] = 'J'
# E o replace não altera a frase, se eu alterar e logo em baixo printar a frase novamente, vai vir a original (Sem Alterações)
# Só valerá minha alteração se eu atribuir o método na variável. Ex: frase = frase.replace('Python', 'Android')
print(frase.replace('Python','Android'))
# Diferente do find, no find ele retornará a posição, aqui retornará True or False
# Mas, e se curso estivesse em lower case?
# print(frase.lower().find('curso'))
print('Curso' in frase)
# Método Upper: Transforma todos os caracteres em CAIXA ALTA, o que já for maiúsculo ele mantém
print(frase.upper())
# Método Lower: Contrário de upper, transforma todos em caixa baixa
print(frase.lower())
# Transforma tudo em lower e deixa apenas o primeiro caractere em upper
print(frase.capitalize())
# Onde tiver espaço ele fará uma quebra de palavras e em todo início de frase ele transforma em upper
print(frase.title())

# Nossos pais têm o hábito de ao preencher algum formulário ele não clica no
# input e começa a digitar, ele clica aperta a barra de espaço algumas x pra
# ver se funciona e assim começa a escrever, isso tem se tornado normal e
# algumas linguagens tem a opção de eliminar esses espaços vagos no início e
# fim pra deixar apenas o essencial
n = input('Digite seu nome: ')
# O strip elimina os espaços vagos inúteis no início e fim
print(n.strip())
# R de Right: Direita.
# Muitas funcoes dentro do python que tratam strings tem a variação R (que começa a tratar pela Direita)
print(n.rstrip())
# L de Left:  Esquerda.
print(n.lstrip())
