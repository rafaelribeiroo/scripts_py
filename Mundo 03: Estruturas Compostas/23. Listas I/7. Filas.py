# Esse modelo é chamado de: "FIFO" (Primeiro Entrar/Primeiro Sair)

# Provê expansão de funções para listas, vai além do pop, remove...
from collections import deque

fila = deque([])

fila.append('Abel')
fila.append('Bruno')
fila.append('Estrangulento')
fila.append('Ximboca')

fila.pop()
# Remove o 1o item da esquerda pra direita
fila.popleft()

# Poderíamos utilizar o insert para inserir no começo da lista, porém pediria
# uns parâmetros adicionais, o que é mais simples pelo appendleft
fila.appendleft('Furão')
