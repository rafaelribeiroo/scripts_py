# A partir desse momento teremos 2 listas na memória, valores e lista; uma vai
# interferir diretamente na outra.


def dobra(lista):
    contador = 0
    while contador < len(lista):
        # Pra cada valor passado pra função, dobre-o.
        lista[contador] *= 2
        contador += 1
    print(lista)


valores = [7, 2, 5, 0, 4]
# A passagem de parâmetro no PY é por referência, ao contrário de C e Java que
# é por valor.
dobra(valores)  # ou dobra([7, 2, 5, 0, 4])
