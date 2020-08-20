'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def título():
    print('Controle de Terrenos')
    print('-' * 30)
def area(a,b):
    print(f'A área de um terreno {l}X{c} é de {l*c}m2')

título()
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO:'))
area(l,c)


