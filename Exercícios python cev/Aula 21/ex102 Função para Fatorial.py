'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(num, show=False):
    '''
    Calcula o fatorial do número pedido
    :param num: número pedido pelo usuário
    :param show: móstra ou não o fatorial
    :return: mostra o calculo do fatorial
    '''
    c = num
    f = 1
    while c > 0:
        if show:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    return f



#Programa principal
num = int(input('Qual número deseja saber o Fatorial? '))
print(fatorial(num, show=False))