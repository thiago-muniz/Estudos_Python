'''
Crie um programa que declare uma matriz de dimensão 3x3 e
preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''
lista0 = []
lista1 = []
lista2 = []
lista = [lista0, lista1, lista2]
for e, c in enumerate(lista):
    if e == 0:
        for E, C in enumerate(lista):
            num = lista0.append(int(input(f'Digite um número para [0 , {E}]:')))
    elif e == 1:
        for E, C in enumerate(lista):
            num = lista1.append(int(input(f'Digite um número para [1 , {E}]:')))
    elif e == 2:
        for E, C in enumerate(lista):
            num = lista2.append(int(input(f'Digite um número para [2 , {E}]:')))
for e, c in enumerate(lista0):
    print(f'[{lista0[e]}] ', end='')
print()
for e, c in enumerate(lista1):
    print(f'[{lista1[e]}] ', end='')
print()
for e, c in enumerate(lista2):
    print(f'[{lista2[e]}] ', end='')



