'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
def título(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f}, de {p} em {p}. ')


def contador(i, f, p):
    if i < f and p == 0:
        p = 1
    elif i > f and p == 0:
        p = -1
    for n in range(i, f+1, p):
        sleep(0.3)
        print(n, end=' ')
    print('FIM!')


#Programa Principal
título(1, 10, 1)
contador(1, 10, 1)
título(10, 0, 2)
contador(10, -2, -2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
título(i, f, p)
contador(i, f, p)
