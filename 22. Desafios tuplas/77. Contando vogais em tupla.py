# 77. Crie um programa que tenha uma tupla com várias palavras (não usar
# acentos). Depois disso, você deve mostrar, para cada palavra, quais
# são as suas vogais.

lista = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'grátis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)

# Primeiro iteramos cada palavra dentro da minha lista
for palavra in lista:
    print(f'\nNa palavra {palavra} temos ', end='')
    # Depois, cada letra da palavra
    for letra in palavra:
        # E fazemos a verificação letra/letra se há alguma vogal
        if letra.lower() in 'aáeéióoóu':
            print(letra, end=' ')
