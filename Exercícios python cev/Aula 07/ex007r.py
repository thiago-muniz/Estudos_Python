aluno = {'Nome:': 'a', 'Nota 1:': 0, 'Nota 2:': 0, 'Média:': 0}
aluno['Nome:'] = str(input('Nome do aluno? '))
aluno['Nota 1:'] = float(input(f'Primeira nota de {aluno["Nome:"]}: '))
aluno['Nota 2:'] = float(input(f'Segunda nota de {aluno["Nome:"]}: '))
aluno['Média:'] = (aluno['Nota 1:'] + aluno['Nota 2:']) / 2
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} tem valor {v}')

