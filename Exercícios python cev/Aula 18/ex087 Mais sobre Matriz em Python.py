'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
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

npar = nmaior = 0
for p, c in enumerate(lista):
    if p == 0:
        for c in lista0:
            if c % 2 == 0:
                npar += c
    elif p == 1:
        for p, c in enumerate(lista1):
            if c % 2 == 0:
                npar += c
            if p == 0:
                nmaior = c
            elif p == 1:
                if c > nmaior:
                    nmaior = c
            elif p == 2:
                if c > nmaior:
                    nmaior = c

    else:
        for c in lista2:
            if c % 2 == 0:
                npar += c
print(f'\nA soma dos números pares é {npar}.')

lista3 = lista0[2] + lista1[2] + lista2[2]
print(f'A soma dos valores da terceira coluna é {lista3}.')
print(f'O maior número da segunda linha é: {nmaior}')
