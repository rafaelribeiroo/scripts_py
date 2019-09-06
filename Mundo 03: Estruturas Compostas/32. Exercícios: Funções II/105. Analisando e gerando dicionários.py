# 105. Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# > Quantidade de notas
# > A maior nota
# > A menor nota
# > A média da turma
# > A situação (opcional)
# Adicione também as docstrings da função.


def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    alunos = dict()
    maior = menor = 0

    alunos['total'] = len(n)
    for posição, elemento in enumerate(n):
        if posição == 0:
            maior = menor = elemento
        else:
            if elemento > maior:
                maior = elemento
            if elemento < menor:
                menor = elemento

    alunos['maior'] = maior
    alunos['menor'] = menor
    alunos['média'] = sum(n) / len(n)
    if sit is True:
        if alunos['média'] < 6.0:
            alunos['situação'] = 'RUIM'
        elif alunos['média'] < 7.0:
            alunos['situação'] = 'RAZOÁVEL'
        elif alunos['média'] > 7.0:
            alunos['situação'] = 'BOA'
    return alunos


resp = notas(3.5, 10, 6.5, sit=True)
help(notas)
