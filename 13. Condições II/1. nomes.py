nome = input('Qual é seu nome? ')
if nome == 'Rafael':
    print('Que nome bonito!')
elif nome == 'Michelangelo' or nome == 'Donatello' or nome == 'Leonardo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
