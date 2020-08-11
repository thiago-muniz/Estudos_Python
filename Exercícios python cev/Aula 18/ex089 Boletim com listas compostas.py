'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''
turma = [] # lista definitiva, para receber as cópias de notasaluno
notasaluno = [] # lista flutuante
r = '' # Para break do loop
while r != 'N':
    aluno = str(input('Nome do aluno: '))
    nota1 = float(input('Primeira nota do aluno: '))
    nota2 = float(input('Segunda nota do aluno: '))
    notasaluno.append(aluno)
    notasaluno.append(nota1)
    notasaluno.append(nota2)
    turma.append(notasaluno[:])
    notasaluno.clear()

    while True:
        r = str(input('Deseja cadastrar mais um aluno? [S / N]')).upper().strip()
        if 'S'  in r:
            break
        if 'N' in r:
            break
print('-' * 30)
print(f'{"NOTAS DA TURMA":^30}')
print('-' * 30)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>15}')
for p, c in enumerate(turma):
    print(f'{p:<5}{c[0]:<10}{(c[1]+c[2])/2:>15}')
print('-' * 30)
m = 0
while m != 999:
    m = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for p, c in enumerate(turma):
        if m == p:
            print(f'As notas de {turma[p][0]} são: {turma[p][1:]}')
            print('-' * 30)
print('FIM DO PROGRAMA')



