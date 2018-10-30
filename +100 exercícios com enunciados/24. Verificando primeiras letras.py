# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO".
cid = str(input('Em que cidade você nasceu? ')).strip()
# Como pede pra verificar se está logo no início eu fatiei minha string
# aos 5 primeiros caracteres afim de verificar se existe Santo no início.
print(cid[:5].upper() == 'SANTO')
