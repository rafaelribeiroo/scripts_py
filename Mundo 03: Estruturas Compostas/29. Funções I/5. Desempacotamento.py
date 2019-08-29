def soma(* valores):
    soma = 0
    # "Desempacotando" os valores recebidos e somando-os
    for núm in valores:
        soma += núm
    print(f'Somando os valores {valores} temos {soma}')


soma(5, 2)
soma(2, 9, 4)
