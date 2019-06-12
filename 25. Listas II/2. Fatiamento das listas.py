galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera[0][0])  # João
print(galera[1][1])  # 33
print(galera[2][0])  # Joaquim
print(galera[1])  # ['Ana', 33]

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
