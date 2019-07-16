nome = input('Qual é seu nome? ').title()

if nome == 'Rafael':
    print('Que nome bonito!')
elif nome == 'Miguel' or nome == 'Gabriel' or nome == 'Guilherme':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
