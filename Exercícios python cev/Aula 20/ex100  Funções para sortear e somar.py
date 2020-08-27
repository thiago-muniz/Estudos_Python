''' Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep
lista = []
def sorteio():
    for n in range(1, 6):
        lista.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end=' ')
    for n in lista:
        print(f'{n} ', end='')
        sleep(0.3)
    print()

def somapar():
    par = 0
    for n in lista:
        if n % 2 == 0:
            par += n
    print(f'A soma dos pares é : ', end='')
    print(f'{par}')


#programa principal:
sorteio()
somapar()