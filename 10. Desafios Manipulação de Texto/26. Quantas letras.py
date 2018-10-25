# 26. Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').lower().strip()
print('Analisando a letra "A", ela aparece {} vezes'.format(frase.count('a')))
# Porque +1 logo após o método find? Porque o Python ignora o último valor,
# considera o 0. O +1 vai para facilitar nossa contagem humana
print('Aparece pela 1ª vez na posição: {}'.format(frase.find('a') + 1))
# Adequar a posição no Python (Já que ele começa no 0)
print('E pela última vez em: {}'.format(frase.rfind('a') + 1))
