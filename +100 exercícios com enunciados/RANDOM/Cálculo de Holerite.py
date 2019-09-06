# Se o usuário não selecionar algum convênio do menu, não cobrará
custo_he = custo_o_prev = custo_inter_o = custo_unimed = custo_gamalu = 0.00
custo_sindicato = custo_PAT = custo_transporte = custo_estacionamento = 0.00
custo_convenio = custo_consulta_1 = custo_consulta_2 = custo_exame_1 = 0.00
custo_exame_2 = custo_exame_3 = custo_terapia = 0.00

print('*' * 6, 'Simulador de cálculo salarial', '*' * 6, end='\n\n')
salário = float(input('Salário bruto (Informe os centavos seguido de .): '))

while True:
    print('''\nAbaixo, os convênios que o ML provê:\n
[ 0 ] Para sair
[ 1 ] Convênio odontológico: OdontoPrev
[ 2 ] Convênio odontológico: InterOdonto
[ 3 ] Convênio médico: Unimed
[ 4 ] Grêmio Desportivo: Gamalu
[ 5 ] Contribuição Assistencial ao Sindicato
[ 6 ] Programa de Alimentação do Trabalhador (PAT)
[ 7 ] Vale transporte
[ 8 ] Estacionamento Agabê
[ 9 ] Cálculo de Horas Extras
   ''')
    benefícios = int(input('Informe: '))

    if benefícios == 0:
        break

    if benefícios == 1:
        valor_prev = 9.98

        dependentes_odontoprev = int(input('\nAlém de você, há quantos '
'dependentes nesse plano? '))
        custo_o_prev = (valor_prev + (valor_prev * dependentes_odontoprev))
        print(f'\nO custo da odontoprev será de {custo_o_prev:.2f}')

    elif benefícios == 2:
        valor_inter = 9.98

        dependentes_interodonto = int(input('\nAlém de você, há quantos '
'dependentes nesse plano? '))
        custo_inter_o = (valor_inter + (valor_inter * dependentes_interodonto))
        print(f'\nO custo da interodonto será de {custo_inter_o:.2f}')

    elif benefícios == 3:
        # Se o usuário esquecer de alguma consulta realizada e decidir
        # incrementar em um segundo loop, vai zerar os valores
        # anteriores
        custo_consulta_1 = custo_consulta_2 = custo_exame_1 = custo_exame_2 = 0
        custo_exame_3 = 0
        # Valor plano
        valor_unimed = 112.50
        # Valores de consultas
        valor_consulta_consultório = 29.00
        valor_consulta_socorro = 34.00
        # Valores exames
        valor_exame_simples = 20.00
        valor_exame_especial = 113.00
        valor_teto_exames = 175.00
        # Valor terapia
        valor_terapia = 23.00

        dependentes_unimed = int(input('\nAlém de você, há quantos dependentes'
' nesse plano? '))
        custo_convenio = (valor_unimed + (valor_unimed * dependentes_unimed))
        valida_consulta = str(input('\nFoi realizada alguma consulta? [S/n] '))
        if valida_consulta in 'Ss':
            qntde_consultas = int(input('Informe quantas: '))
            print('''[ 1 ] Consulta em consultório
[ 2 ] Consulta em pronto socorro''')
            for contador in range(1, qntde_consultas + 1):
                tipo_consulta = int(
                    input(f'Informe o tipo da {contador}ª consulta: ')
                )
                if tipo_consulta == 1:
                    custo_consulta_1 += valor_consulta_consultório
                elif tipo_consulta == 2:
                    custo_consulta_2 += valor_consulta_socorro
        valida_exame = str(input('\nE exame(s)? [S/n] '))
        if valida_exame in 'Ss':
            qntde_exames = int(input('Quantas pessoas fizeram exames? '))
            for contador in range(1, qntde_exames + 1):
                qntde_pessoas_examinadas = int(
                    input(f'Informe quantos exames a {contador}ª pessoa fez: ')
                )
                print('''[ 1 ] Exame simples
[ 2 ] Exame especial
''')
                for contador_2 in range(1, qntde_pessoas_examinadas + 1):
                    tipo_exame = int(
                        input(f'Informe o tipo do {contador}º exame: ')
                    )
                    if tipo_exame == 1:
                        custo_exame_1 += valor_exame_simples
                    elif tipo_exame == 2:
                        custo_exame_2 += valor_exame_especial
                if (custo_exame_1 + custo_exame_2) >= valor_teto_exames:
                    custo_exame_1 = custo_exame_2 = 0.00
                    custo_exame_3 += valor_teto_exames
        valida_terapia = str(input('\nE terapia(s)? [S/n] '))
        if valida_terapia in 'Ss':
            qntde_terapias = int(input('Informe quantas: '))
            custo_terapia = (qntde_terapias * valor_terapia)

        custo_unimed = custo_convenio + custo_consulta_1 + custo_consulta_2
        + custo_exame_1 + custo_exame_2 + custo_exame_3 + custo_terapia
        print(f'\nO custo da unimed será {custo_unimed:.2f}')

    elif benefícios == 4:
        custo_gamalu = 22.80
        print(f'\nO custo do gamalu será de {custo_gamalu:.2f}')

    elif benefícios == 5:
        # Para quem não paga mais, será 0
        custo_sindicato = 0.00
        piso_valor_sindicato = 70.00
        teto_valor_sindicato = ((salário * 2) / 100)

        valida_sindicato = str(
            input('\nVocê levou a carta de oposição ao desconto das '
'contribuições ao sindicato? [S/n] ')
        )
        if valida_sindicato in 'Nn':
            if salário <= 3500:
                custo_sindicato = piso_valor_sindicato
            else:
                custo_sindicato = teto_valor_sindicato
        print(f'\nO custo do sindicato será de {custo_sindicato:.2f}')

    elif benefícios == 6:
        benefício_alimentação = float(
            input('\nInforme quanto recebeu de Ticket Alimentação/Refeição: '
'R$'))
        custo_PAT = ((benefício_alimentação * 1) / 100)
        print(f'\nO custo da PAT será de {custo_PAT:.2f}')

    elif benefícios == 7:
        custo_transporte = ((salário * 6) / 100)
        print(f'\nO custo do transporte será de {custo_transporte:.2f}')

    elif benefícios == 8:
        valor_moto = 25.00
        valor_carro = 70.00

        veículo = str(input('''\nVocê vêm ao serviço de quê?
[ M ] Moto
[ C ] Carro
  '''))[0]
        while veículo not in 'MmCc':
            veículo = str(input('Opção inválida, tente novamente: '))[0]
            if veículo in 'MmCc':
                break
        if veículo in 'Mm':
            custo_estacionamento = valor_moto
        elif veículo in 'Cc':
            custo_estacionamento = valor_carro
        print('\nO custo do estacionamento será de '
        f'{custo_estacionamento:.2f}')

    elif benefícios == 9:
        jornada = int(input('Qual a sua jornada de horas mensais? [180/220] '))
        while jornada != 180 and jornada != 220:
            jornada = int(input('Opção inválida, tente novamente: '))
        hora = salário / jornada
        qntde_total_he = float(input('Quantas horas extras você fez? '))
        while True:
            calcule = str(input('''[ 1 ] para calcular horas extras
[ 0 ] para sair
  '''))
            if calcule in '1':
                qntde60 = float(input('Quantas horas extras de 60%? '))
                cálculo60 = (hora + (hora * 60) / 100) * qntde60
                qntde100 = float(input('Quantas 100%? '))
                cálculo100 = (hora + (hora * 100) / 100) * qntde100
            if calcule in '0':
                custo_he = cálculo60 + cálculo100
                if (qntde60 + qntde100) == qntde_total_he:
                    break
                if (qntde60 + qntde100) != qntde_total_he:
                    print('Falta calcular algumas HE, refaça!')
        print(f'Pelas horas extras, receberá R${custo_he:.2f}')

# Totalizando o salário e horas extras para saber quanto INSS/IRRF debitará
salário += custo_he

custo_despesas = custo_o_prev + custo_inter_o + custo_unimed + custo_gamalu
+ custo_sindicato + custo_PAT + custo_transporte + custo_estacionamento

# Tabela de contribuição mensal 2019
if salário <= 1751.81:
    inss = ((salário * 8) / 100)
elif salário <= 2919.72:
    inss = ((salário * 9) / 100)
elif salário <= 5839.45:
    inss = ((salário * 11) / 100)
print(f'O desconto do INSS é de R$ {inss:.2f}')

# Tabela de incidência mensal 2019
if salário <= 1903.98:
    irpf = 0.00
elif salário <= 2826.65:
    irpf = ((salário * 7.5) / 100)
elif salário <= 3751.05:
    irpf = ((salário * 15) / 100)
elif salário <= 4664.68:
    irpf = ((salário * 22.5) / 100)
elif salário > 4664.68:
    irpf = ((salário * 27.5) / 100)
print('O desconto do IRPF é de R$ {:.2f}'.format(irpf))

print(f'Pelo que foi informado, você receberia R${salário}, mas com base nas '
f'despesas de R${custo_despesas:.2f}, você vai ficar com '
f'{salário - custo_despesas:.2f}')
