num = [2, 5, 9, 1]

# Inserção de um novo elemento na lista
num.append(7)
# Ordenar do menor pro maior
num.sort()
# Ordenação reversa
num.sort(reverse=True)
# No 1º informamos a posição que será inserido o 2º parâmetro
num.insert(2, 0)
# Quantos elementos possuo na lista
print(f'Essa lista tem {len(num)} elementos')
