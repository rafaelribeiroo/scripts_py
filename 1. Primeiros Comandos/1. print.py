#Se os dados forem mensagem HÁ delimitadores, pode ser ' ou "
print('Olá, mundo!')

#Se forem números não HÁ
print(7+4)

#Ele não fará a soma aqui pois como há delimitadores ele entende isso como uma mensagem e apenas concatena: transformando em 74
print('7' + '4')

# Se eu tentar printar apresentando mensagens e números com soma dará erro porque a soma apenas junta se forem ambos do mesmo tipo
#print('Olá' + 5)

# Aqui dá certo mesmo sendo tipos diferentes porque foram separados com ,
print('Olá', 5)

