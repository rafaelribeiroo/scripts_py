# 77. Crie um programa que tenha uma tupla com várias palavras (não usar
# acentos). Depois disso, você deve mostrar, para cada palavra, quais
# são as suas vogais.

lista = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'grátis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)

for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aáeéióoóu':
            print(letra, end=' ')
