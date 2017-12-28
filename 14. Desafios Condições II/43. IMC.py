#43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- 25 até 30: Sobrepeso
#- Acima de 40: Obesidade mórbida
peso = float(input('Qual é seu peso?  (Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = peso / (alt ** 2) #Or alt * alt
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do PESO normal')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade!')
elif imc >= 40:
    print('Obesidade mórbida')
