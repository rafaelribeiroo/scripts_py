# 26. Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').upper().strip()

print(f"Analisando a letra 'A', ela aparece {frase.count('A')} vezes")
# Porque +1? Porque o Python ignora o último valor, considerando o 0
print(f"Aparece pela 1ª vez na posição: {frase.find('A') + 1}")
# Adequar a posição no Python
print(f"E pela última vez em: {frase.rfind('A') + 1}")
