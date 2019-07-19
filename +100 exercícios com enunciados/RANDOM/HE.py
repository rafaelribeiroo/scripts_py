# from time import sleep

print('{:*^40}'.format('M A G A Z I N E'))

# Altere os preços aqui, para não ter que mudar em 30 variáveis diferentes
preço_interodonto = 16.00
preço_odontoprev = 19.17

preço_unimed = 112.50
consulta_consultorio = consulta_prontosocorro = 0.00
exame_simples = exame_especial = total_exame = 0.00
terapia = 0.00

# Apenas se o usuário selecionar, incrementará com o valor adequado
odontoprev = interodonto = gamalu = pat = sdt = transporte = trans_hb = 0.00
he_final = somatório = 0

print('*' * 6, 'Simulador de cálculo salarial', '*' * 6, end='\n\n')
sal = float(input('Salário bruto [. pros centavos]: '))

jornada = int(input('Qual a sua jornada de horas mensais? [180/220] '))
while jornada != 180 and jornada != 220:
    jornada = int(input('Opção inválida, tente novamente: '))

# Calculando valor da sua hora
hora_valor = sal / jornada

# Cálculo da porcentagem INSS
if sal <= 1693.72:
    # Se você receber entre os valores acima, sua alíquota será de 8
    inss = ((sal * 8) / 100)
elif sal > 1693.72 and sal <= 2822.90:
    # A alíquota será de 9
    inss = ((sal * 9) / 100)
elif sal > 2822.90 and sal <= 5645.80:
    # A alíquota será de 11
    inss = ((sal * 11) / 100)
elif sal > 5645.80:
    # A alíquota será R$621,04 fixa
    inss = (621.04)

print('\nO desconto do INSS é de R$ {:.2f}'.format(inss))

# Cálculo do Imposto sobre a renda das pessoas físicas
# Tabela de incidência mensal 2018
if sal <= 1903.98:
    # Não paga imposto de renda
    irpf = (0.00)
elif sal > 1903.99 and sal <= 2826.65:
    # A alíquota será de 7.5
    irpf = ((sal * 7.5) / 100)
elif sal > 2826.66 and sal <= 3751.05:
    # A alíquota será de 15
    irpf = ((sal * 15) / 100)
elif sal > 3751.05 and sal <= 4664.68:
    # A alíquota será de 22.5
    irpf = ((sal * 22.5) / 100)
else:
    # A alíquota será de 27.5
    irpf = ((sal * 27.5) / 100)

print('O desconto do IRPF é de R$ {:.2f}'.format(irpf))

while True:
    print('''\n> Selecione, se você possui algum desconto legal abaixo:
    [ -1 ] Para sair
    [  1 ] Convênio odontológico: OdontoPrev
    [  2 ] Convênio odontológico: InterOdonto
    [  3 ] Convênio médico: Unimed
    [  4 ] Grêmio Desportivo: Gamalu
    [  5 ] Contribuição Assistencial (Sindicato)
    [  6 ] PAT - Lei 6.321/76
    [  7 ] Vale transporte
    [  8 ] Estacionamento Agabê
    [  9 ] Cálculo de Horas Extras
    ''')
    benefícios = int(input('Digite um de cada vez: '))
    if benefícios < 0:
        print('Saindo do menu, aguarde 3seg.')
        # sleep(3)
        break

    # Condição pronta
    if benefícios == 1:
        dep_odonto = int(input('\nAlém de você, há quantos' +
                               ' dependentes nesse plano? '))
        odontoprev = (preço_odontoprev + (preço_odontoprev * dep_odonto))
        print(f'\nO desconto do odontoprev é de {odontoprev:.2f}')
        # sleep(3)

    # Condição pronta
    elif benefícios == 2:
        dep_inter = int(input('\nAlém de você, há quantos' +
                              ' dependentes nesse plano? '))
        interodonto = (preço_interodonto + (preço_interodonto * dep_inter))
        print(f'\nO desconto da interodonto é de {interodonto:.2f}')
        # sleep(3)

    # Condição pronta
    elif benefícios == 3:
        dep_unimed = int(input('\nAlém de você, há quantos' +
                               ' dependentes nesse plano? '))
        unimed = (preço_unimed + (preço_unimed * dep_unimed))

        consulta_bool = str(input(
            'Foi realizado alguma consulta? [s/n] ')
        ).lower().strip()[0]
        if consulta_bool == 's':
            consultas = int(input('Informe quantas: '))
            print('''\n>> Selecione o tipo de consulta:
[ 1 ] Consulta em consultório
[ 2 ] Consulta em pronto socorro
        ''')
            for c in range(1, consultas + 1):
                tipo_consulta = int(
                    input(f'Informe o tipo da {c}ª consulta: ')
                )
                if tipo_consulta == 1:
                    consulta_consultorio += 29.00
                elif tipo_consulta == 2:
                    consulta_prontosocorro += 34.00

        exame_bool = str(
            input('E exame(s)? [s/n] ')
        ).lower().strip()[0]
        if exame_bool == 's':
            qntde_pessoas_examinadas = int(
                input('Quantas pessoas fizeram exames? ')
            )
            for cont1 in range(1, qntde_pessoas_examinadas + 1):
                exames = int(
                    input(f'Informe quantos exames a {cont1}ª pessoa fez: ')
                )
                print('''\n>> Selecione o tipo de exame:
[ 1 ] Exame simples
[ 2 ] Exame especial
        ''')
                for cont2 in range(1, exames + 1):
                    tipo_exame = int(
                        input(f'Selecione o tipo do {cont2}º exame: ')
                    )
                    if tipo_exame == 1:
                        exame_simples += 20.00
                    elif tipo_exame == 2:
                        exame_especial += 113.00
                if exame_simples + exame_especial >= 175.00:
                    exame_simples = exame_especial = 0
                    total_exame += 175.00

        # If terapias realizadas
        terapia_bool = str(
            input('E terapia(s)? [s/n] ')
        ).lower().strip()[0]
        if terapia_bool == 's':
            terapias = int(input('Informe quantas: '))
            terapia = (terapias * 23.00)
        somatório = unimed + consulta_consultorio + consulta_prontosocorro
        + exame_simples + exame_especial + total_exame + terapia
        print(f'\nO desconto total da unimed é de {somatório:.2f}')
        # sleep(3)

    # Condição pronta
    elif benefícios == 4:
        gamalu = (21.83)
        print(f'\nO desconto do gamalu é de {gamalu:.2f}')
        # sleep(3)

    # Condição pronta
    elif benefícios == 5:
        if sal <= 3500:
            sdt = ((sal * 2) / 100)
        else:
            sdt = (70.00)
        print(f'\nO desconto do sindicato é de {sdt:.2f}')
        # sleep(3)

    # Condição pronta
    elif benefícios == 6:
        alimentação = float(
            input('Ticket alimentação bruto, cheque o horário para descobir: ')
        )
        pat = ((alimentação * 1) / 100)
        print(f'\nO desconto do PAT é de {pat:.2f}')
        # sleep(3)

    # Condição pronta
    elif benefícios == 7:
        transporte = (sal * 6) / 100  # 6% do salário total
        print(f'\nO desconto do transporte é de {transporte:.2f}')
        # sleep(3)

    elif benefícios == 8:
        print('Você vem de moto ou carro?', end=' ')
        escolha = str(input('')).upper().strip()[0]
        if escolha == 'M':
            trans_hb = 25.00
        elif escolha == 'C':
            trans_hb = 70.00
        else:
            print('Veículo não compreensível')
        print(f'\nO desconto do estacionamento é de {trans_hb:.2f}')
        # sleep(3)

    elif benefícios == 9:
        he_qntde = float(input('Quantas horas extras você fez? '))
        while True:
            calcular_primeiro = str(
                input('Escolha qual deseja calcular: [60/100/S]')
            )
            if calcular_primeiro == '60':
                he_60 = float(input('Quantas 60%? '))
            elif calcular_primeiro == '100':
                he_100 = float(input('E 100%? '))
            else:
                break
        calculo_60 = (hora_valor * 60) / 100
        final_60 = calculo_60 * he_60
        calculo_100 = (hora_valor * 100) / 100
        final_100 = calculo_100 * he_100
        he_final = final_60 + final_100
        print(f'Horas extras vão somar R${he_final:.2f}')

# Cálculo das despesas
despesas = inss + irpf + odontoprev + interodonto + somatório + gamalu + sdt
+ pat + transporte


print(f'\n\nSalário Bruto: {sal:.2f}' +
      f'\nTendo em base que o INSS te custou R$ {inss:.2f}' +
      f'\nIRPF R$ {irpf:.2f}' +
      f'\nOdontoprev R$ {odontoprev:.2f}' +
      f'\nInterodonto R$ {interodonto:.2f}' +
      f'\nUnimed R$ {somatório:.2f}' +
      f'\nGamalu R$ {gamalu:.2f}' +
      f'\nSindicato R$ {sdt:.2f}' +
      f'\nPAT R$ {pat:.2f}' +
      f'\nE transporte R$ {transporte:.2f}' +
      f'\nO total dá uma soma de R$ {despesas:.2f}' +
      f'\nO total de hora extra equivale a R$ {he_final:.2f}')
