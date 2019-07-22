# A partir desse momento teremos 2 listas na memória, sendo uma: 'valores', e a
# outra: 'lista'. Uma vai interferir diretamente na outra.
def dobra(lista):
    posição = 0
    while posição < len(lista):
        lista[posição] *= 2
        posição += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
# Passagem de parâmetro no PY é por referência, ao contrário de C e Java que é
# por valor.
