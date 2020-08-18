'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
pessoas = []
pessoa = {}
from operator import itemgetter
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:                             #add persons gender to the dict, and only accept F or M as awnser
        pessoa['Sexo'] = str(input('Sexo:[F / M]')).upper().strip()
        if pessoa['Sexo'] in 'FM':
            break
        else:
            print('Opção inválida.')

    pessoa['Idade'] = int(input('Idade: '))  #add persons age to the dict
    pessoas.append(pessoa.copy())            #add the dict to the list

    while True:
        continuar = str(input('Deseja cadastrar mais uma pessoa?[S/N] ')).upper().strip()
        if continuar in 'SN':
            break
        else:
            print('Opção inválida.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A)Ao todo temos {len(pessoas)} cadastradas')

s = 0
for p in pessoas:
    s = s +(p['Idade'])
média = s/len(pessoas)
print(f'B) A média de idade é de: {média} anos')

listamulheres = []
for p in pessoas:
    if p['Sexo'] == 'F':
        listamulheres.append(p)
print('C) As mulheres cadastradas foram: ', end=' ')
for p in listamulheres:
    print(f'{p["Nome"]}', end=' ')

print('\nD) Lista das pessoas que estão acima da média')
acimamedia = []
for p in pessoas:
    if p['Idade'] > média:
        acimamedia.append(p)
for p in acimamedia:
    for k, v in p.items():
        print(f'{k} = {v}  ', end=" ")
print('\n')
print('<< FINALIZADO >>')
