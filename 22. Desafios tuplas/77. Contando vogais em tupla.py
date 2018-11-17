# 77. Crie um programa que tenha uma tupla com várias palavras (não usar
# acentos). Depois disso, você deve mostrar, para cada palavra, quais
# são as suas vogais.
palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'grátis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    # Nosso for acima é de palavra em palavra
    # Aqui pegamos a palavra e damos um loop para obter os caracteres
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra, end=' ')
