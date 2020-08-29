# Programa exercício aleatório do dia
# Sorteio de um exercício aleatório do curso em video de Python para praticar e refazer

from random import randint
print('-' * 30)
print('    Curso em Vídeo Python    ')
print('-' * 30)
while True:
    mundo = int(input('''De qual mundo você gostaria de realizar um exercício:
1) Mundo 1 - Fundamentos
2) Mundo 2 - Estruturas de Controle
3) Mundo 3 - Estruturas Compostas 
4) Qualquer Mundo
'''))
    if mundo == 1:
        num = randint(1, 35)
        print(f'Você deverá fazer o exercício {num} hoje!')
        break
    elif mundo == 2:
        num = randint(36, 71)
        print(f'Você deverá fazer o exercício {num} hoje!')
        break
    elif mundo == 3:
        num = randint(71, 114)
        print(f'Você deverá fazer o exercício {num} hoje!')
        break
    elif mundo == 4:
        num = randint(1, 114)
        print(f'Você deverá fazer o exercício {num} hoje!')
        break
    else:
        print('Resposta inválida')
print('<< BOM ESTUDO >>')

