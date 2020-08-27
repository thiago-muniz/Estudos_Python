'''
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

from datetime import date

def voto(a):
    if 18 <= a <= 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif a < 18:
        print(f'Com {idade} anos: VOTO NEGADO')
    elif a > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')


#Programa Principal
ano = int(input('Qual o ano de nascmento? '))
idade = date.today().year - ano
voto(idade)