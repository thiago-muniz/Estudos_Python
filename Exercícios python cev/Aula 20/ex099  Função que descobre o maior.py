'''
 Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
def maior(*num):
    nmaior = 0
    print('-_' * 30)
    print('Analisando os valores passados...')
    for pos, n in enumerate(num):
        print(n, end=' ')
        sleep(0.3)
        if pos == 0:
            nmaior = n
        elif pos >= 1:
            if n > nmaior:
                nmaior = n

    print()
    if len(num) == 1 and 0 in num:
        print(f'Foram informados {0} valores ao todo.')
    elif len(num) >= 1:
        print(f'Foram informados {len(num)} valores ao todo.')
    sleep(1)
    print(f'O maior número informado foi {nmaior}')
    sleep(1)


#programa principal
maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(0)
maior(1)