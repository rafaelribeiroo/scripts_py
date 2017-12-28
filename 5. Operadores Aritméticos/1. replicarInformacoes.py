nome = input('Qual é seu nome? ')
#Abaixo esses códigos dentro das chaves indica que ele vai usar 20 espaços para escrever o meu nome, o circunflexo irá centralizar a variável e o sinal de igual vai inserir ele nos outros espaços em branco
print('Prazer em te conhecer {:=^20}!'.format(nome))
#Abaixo desloco meu nome ao final da linha, direita
print('Prazer em te conhecer {:>20}!'.format(nome))
#Abaixo movo meu nome pro começo da linha, esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
