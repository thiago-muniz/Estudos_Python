'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''

lista = []

for c in range(0,7):
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        numpar = 2
    if num % 2 == 1:
        numimpar = 1
lista.sort()
if numpar == 2:
    print(f'A lista de números pares em ordem crescente: ')
    for c in lista:
        if c % 2 == 0:
            print(f'{c}', end=' ')
if numimpar == 1:
    print(f'\nA lista de números ímpares em ordem crescente: ')
    for c in lista:
        if c % 2 == 1:
            print(f'{c}', end=' ')