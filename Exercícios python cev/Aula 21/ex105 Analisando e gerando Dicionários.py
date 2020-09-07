'''
 Faça um programa que tenha uma função notas() que pode receber várias notas de
 alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

'''
def notas(*num, sit=False):
    '''
    O programa recebe notas de uma aluno, mostrando quantidade de notas, a média entre elas e a situação
    do aluno.
    A avaliação é mostrada através de um dicionário.
    :param num: desempacota os números fornecidos pelo usuário
    :param sit: Registra ou não o campo 'Situação' no dicionário
    :return: retona os dados gerados em forma de dicionário
    '''
    dicioaluno = {'Total': 0, 'Menor': 0, 'Maior': 0, 'Média': 0}
    cont = 0
    soma = 0
    maior = menor = 0
    for n in num:
        soma += n   #Soma as notas
        if cont == 0:   #Avalia os maiores e menores dentro de num
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        cont += 1   #conta número de notas e número de laços
    média = soma / cont #Faz a média da soma das notas com o número de notas

    dicioaluno['Total'] = cont
    dicioaluno['Média'] = média
    dicioaluno['Menor'] = menor
    dicioaluno['Maior'] = maior
    if sit == True:
        if 5 <= média <= 6.9 :
            dicioaluno['Situação'] = 'Razoável'
        elif 7 <= média <= 10:
            dicioaluno['Situação'] = 'Boa'
        else:
            dicioaluno['Situação'] = 'Deplorável'


    return dicioaluno


#Programa principal
resp = notas(5, 2, sit=True)
print(resp)
print('-_-' * 26)
help(notas)