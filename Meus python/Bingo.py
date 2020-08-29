# Programa Sorteio de Bingo
# Sorteio de 14 números aleatórios entre 1 e 75 para jogadores de bingo

from random import randint
from time import sleep

númerossorteados = list()
cont = 1
while cont <= 24:

    while True:
        num = randint(1, 75)
        if num not in númerossorteados:
            print(f'Bola número {cont}: {num}')
            cont += 1
            númerossorteados.append(num)
            sleep(0.5)
        if cont >= 24:
            break
númerossorteados.sort()
print('Os números sortedos foram: ')
print(f'{númerossorteados}')

