número = somatório = 0

# Laço infinito
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    somatório += n

# PYthon Enhancement Proposal
# F-String (Interpolação) a partir do PY 3.6
print(f'A soma vale {somatório}')
