# PYthon Enhancement Proposal
# Proposta de melhoria do PYthon
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# soma -= 999
# F-String (Interpolação) a partir do PY 3.6
print(f'A soma vale {s}')

# print(f'A soma vale {s:.2f}')
# print(f'A soma vale {s:*^20}')
