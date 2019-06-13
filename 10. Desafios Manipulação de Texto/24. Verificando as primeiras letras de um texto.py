# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
# com o nome "SANTO".

cidade = str(input('Em que cidade você nasceu? ')).strip()

# Como pede pra verificar se está logo no início eu fatiei minha string aos 5
# primeiros caracteres a fim de verificar se existe Santo no início.
print(cidade[:5].upper() == 'SANTO')
