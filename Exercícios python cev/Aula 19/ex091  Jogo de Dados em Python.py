'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from operator import itemgetter
pdicio = dict()
print('Valores Sorteados:')
pdicio = {'Jogador 1': randint(1, 6),
          'jogador 2': randint(1, 6),
          'Jogador 3': randint(1, 6),
          'Jogador 4': randint(1, 6)}
rank = list()
for k, v in pdicio.items():
    print(f'O {k} tirou {v} no dado.')
rank = sorted(pdicio.items(), key=itemgetter(1), reverse=True)
print('-=' * 25)
print(f'{"== RANKING DOS JOGADORES == ":^40}')
for i, v in enumerate(rank):
    print(f'{i+1}º colocado foi {v[0]} com valor {v[1]}. ')

