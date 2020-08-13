'''
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
dicio = {}
dicio['Nome'] = str(input('Nome do aluno: '))
dicio['Média'] = float(input(f'Média de {dicio["Nome"]}: '))
print('-' * 30)
print(f'- nome é igual a {dicio["Nome"]}')
print(f'- média é igual a {dicio["Média"]}')
if dicio['Média'] < 5:
    print('- a situação é igual a REPROVADO.')
elif dicio['Média'] >=5  and dicio['Média'] < 7:
    print('- a situação é igual a RECUPERAÇÃO.')
elif dicio['Média'] >=7 and dicio['Média'] <=10:
    print('- a situação é igual a APROVADO.')
else:
    print('Essa média não existe')