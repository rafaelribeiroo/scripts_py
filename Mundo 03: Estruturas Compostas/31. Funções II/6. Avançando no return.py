# O return não necessariamente é usado apenas para devolver valores numéricos,
# mas também booleanos, listas, strings...


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
