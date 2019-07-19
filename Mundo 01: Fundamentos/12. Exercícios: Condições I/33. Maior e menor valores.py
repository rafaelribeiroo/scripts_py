# 33. Faça um programa que leia três números e mostre qual é o maior e qual é o
# menor.

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
# Porque receber o primeiro input em uma variável que conterá o menor?
# Nós poupamos um pouco o if, se for realmente o 1º. Deu sorte! Caso contrário,
# cairá nas demais condições dos outros if's
# Saber quando colocar algo fora da estrutura de condição é algo importante
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
