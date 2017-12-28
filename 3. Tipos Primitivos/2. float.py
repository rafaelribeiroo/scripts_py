#Qual a diferença entre Decimal, Float e Double?
#Float e Double trabalham com arredondamento de valores, são utilizados quando você não se importa com arredondamento
#Já no Decimal é diferente, utilizam quando necessitamos de uma precisão exata de valores (Dinheiro)
#Float (7 díg. 32bit)
#Double (15-16 díg. 64bit)
#Decimal (28-29 díg. 128bit)
n = float(input('Digite um valor: '))
print(n)
