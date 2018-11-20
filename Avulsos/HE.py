'''Adicional noturno
turno = str(input('Em qual turno você trabalha? [Manhã] ')).lower().strip()[:3]
while turno != 'man' and turno != 'tar' and turno != 'noi' and turno != 'mad':
    turno = str(input('Opção inválida, tente novamente: ')).lower().strip()[:3]
    if turno in 'man':  # Manhã
        adc_noturno = 0
    elif turno in 'tar':  # Tarde
        adc_noturno = 0
    elif turno in 'noi':  # Noite
        adc_noturno = 1
    elif turno in 'mad':  # Madrugada
        adc_noturno = 1'''
from time import sleep

# Altere os preços aqui, para não ter que mudar em 30 variáveis diferentes
preço_interodonto = 16.00
preço_odontoprev = 19.17

preço_unimed = 112.50
consulta_consultorio = consulta_prontosocorro = 0.00
exame_simples = exame_especial = total_exame = 0.00
terapia = 0.00

# Apenas se o usuário selecionar, incrementará com o valor adequado
odontoprev = interodonto = gamalu = pat = sindicato = transporte = 0.00

cont1 = cont2 = cont3 = cont4 = cont5 = 0

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
    [  7 ] O que significa a opção 6?
    [  8 ] Vale transporte
    ''')
    benefícios = int(input('Digite um de cada vez: '))
    if benefícios < 0:
        print('Saindo do menu, aguarde 3seg.')
        sleep(3)
        break
    # Condição pronta
    if benefícios == 1:
        cont1 += 1
        if cont1 == 1:
            dep_odonto = int(input('\nAlém de você, há quantos' +
                                   ' dependentes nesse plano? '))
            odontoprev = (preço_odontoprev + (preço_odontoprev * dep_odonto))
            print(f'\nO desconto do odontoprev é de {odontoprev:.2f}')
            sleep(3)
        else:
            print('Você já selecionou esse convênio anteriormente.')
            sleep(3)
    # Condição pronta
    elif benefícios == 2:
        cont2 += 1
        if cont2 == 1:
            dep_inter = int(input('\nAlém de você, há quantos' +
                                  ' dependentes nesse plano? '))
            interodonto = (preço_interodonto + (preço_interodonto * dep_inter))
            print(f'\nO desconto da interodonto é de {interodonto:.2f}')
            sleep(3)
        else:
            print('Você já selecionou esse convênio anteriormente.')
            sleep(3)

    # Condição pronta
    elif benefícios == 3:
        cont3 += 1
        if cont3 == 1:
            dep_unimed = int(input('\nAlém de você, há quantos' +
                                   ' dependentes nesse plano? '))
            unimed = (preço_unimed + (preço_unimed * dep_unimed))

            # If consultas realizadas
            consulta_bool = str(input('Você ou algum dependente realizou alguma consulta este mês? [s/n] ')).lower().strip()[0]
            if consulta_bool == 's':
                consultas = int(input('Informe quantas: '))
                print('''\n>> Selecione o tipo de consulta:
[ 1 ] Consulta em consultório
[ 2 ] Consulta em pronto socorro
            ''')
                for c in range(1, consultas + 1):
                    tipo_consulta = int(input(f'Informe o tipo da {c}ª consulta: '))
                    if tipo_consulta == 1:
                        consulta_consultorio += 29.00
                    elif tipo_consulta == 2:
                        consulta_prontosocorro += 34.00

            # If exames realizados
            exame_bool = str(input('Você ou algum dependente realizou algum exame este mês? [s/n] ')).lower().strip()[0]
            if exame_bool == 's':
                exames = int(input('Informe quantos: '))
                print('''\n>> Selecione o tipo de exame:
[ 1 ] Exame simples
[ 2 ] Exame especial
            ''')
                for c in range(1, exames + 1):
                    tipo_exame = int(input(f'Selecione o tipo do {c}º exame: '))
                    if tipo_exame == 1:
                        exame_simples += 20.00
                    elif tipo_exame == 2:
                        exame_especial += 113.00
                if exame_simples + exame_especial >= 175.00:
                    total_exame = 175.00

            # If terapias realizadas
            terapia_bool = str(input('Você ou algum dependente realizou alguma terapia este mês? [s/n] ')).lower().strip()[0]
            if terapia_bool == 's':
                terapias = int(input('Informe quantas: '))
                terapia = (terapias * 23.00)
        else:
            print('Você já selecionou esse convênio anteriormente.')
            sleep(3)
        somatório = unimed + consulta_consultorio + consulta_prontosocorro + exame_simples + exame_especial + total_exame + terapia
        print(f'\nO desconto total da unimed é de {somatório:.2f}')
        sleep(3)

    # Condição pronta
    elif benefícios == 4:
        cont4 += 1
        if cont4 == 1:
            gamalu = (21.83)
        else:
            print('Você já selecionou esse convênio anteriormente.')
            sleep(3)
        print(f'\nO desconto do gamalu é de {gamalu:.2f}')
        sleep(3)

    # Condição pronta
    elif benefícios == 5:
        if sal <= 3500:
            sindicato = ((sal * 2) / 100)
        else:
            sindicato = (70.00)
        print(f'\nO desconto do sindicato é de {sindicato:.2f}')
        sleep(3)

    # Condição pronta
    elif benefícios == 6:
        alimentação = float(input('Ticket alimentação bruto, cheque o horário para descobir: '))
        pat = ((alimentação * 1) / 100)
        print(f'\nO desconto do PAT é de {pat:.2f}')
        sleep(3)

    # Condição pronta
    elif benefícios == 7:
        print('''Assim, consiste em um programa de alimentação do colaborador, a empresa
adere a esse programa oferecendo refeitórios próprios ou contratar empresas
prestadoras de serviços de alimentação coletiva. Pode optar também fornecendo
vale alimentação ou refeição. Quer saber mais? Basta copiar e colar esse link
em seu navegador: https://www.youtube.com/watch?v=z11hu8n1phI''')

    # Condição pronta
    elif benefícios == 8:
        cont5 += 1
        if cont5 == 1:
            transporte = (sal * 6) / 100  # 6% do salário total
        else:
            print('Você já selecionou esse convênio anteriormente.')
            sleep(3)
        print(f'\nO desconto do transporte é de {transporte:.2f}')
        sleep(3)

print('\nAdm de Pessoal (Saldo banco de horas) → Nesse programa, vou considerar suas HE como 60%')
he = float(input('Horas extras: '))

# Calculando valor da sua hora extra
# Pego o valor da hora normal + 60% para obter o valor da minha hora extra
hora_extra_valor = hora_valor + (hora_valor * 60) / 100

# Cálculo do quanto você ganhará com sua hora extra
valor_final_he = hora_extra_valor * he

# Somando as receitas (salário + horas_extras)
sal = sal + valor_final_he

# Cálculo das despesas
despesas = inss + irpf + odontoprev + interodonto + somatório + gamalu + sindicato + pat + transporte

print(f'\n\nTendo em base que o INSS te custou R$ {inss:.2f}' +
      f'\nIRPF R$ {irpf:.2f}' +
      f'\nOdontoprev R$ {odontoprev:.2f}' +
      f'\nInterodonto R$ {interodonto:.2f}' +
      f'\nUnimed R$ {somatório:.2f}' +
      f'\nGamalu R$ {gamalu:.2f}' +
      f'\nSindicato R$ {sindicato:.2f}' +
      f'\nPAT R$ {pat:.2f}' +
      f'\nE transporte R$ {transporte:.2f}' +
      f'\nO total dá uma soma de R$ {despesas:.2f}')

print(f'Baseado em todas as suas despesas e horas extras (60%), seu salário final será de: R$ {sal - despesas:.2f}')
