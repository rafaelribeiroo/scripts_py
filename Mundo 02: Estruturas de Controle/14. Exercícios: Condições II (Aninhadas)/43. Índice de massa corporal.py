# 43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo:
# > Abaixo de 18.5: Abaixo do peso
# > Entre 18.5 e 25: Peso ideal
# > 25 até 30: Sobrepeso
# > Acima de 40: Obesidade mórbida

peso = float(input('Qual é seu peso?  (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)  # Ou alt * alt
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    # Para compreensão acima, à direita não muda, à esquerda devemos redigir a
    # expressão de trás pra frente, no caso, >= 18.5.
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
