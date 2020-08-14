'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint

pdicio = dict()
rank = []
rank2 = []

print('Valores Sorteados:')
for c in range(1, 5):
    pdicio[f'Jogador {c}'] = randint(1, 6)
    rank.append(pdicio.copy())
    for k, v in pdicio.items():
        print(f'O {k} tirou {v} no dado.')
    del pdicio[f'Jogador {c}']

maior = menor = 0
print(rank)
for item in rank:
    for v in item.values():
        if len(rank2) == 0:
            maior = menor = v
            rank2.append(item)

        elif len(rank2) == 1:
            if v <= maior:
                rank2.insert(0, item)
            elif v < menor:
                rank2.insert(0, item)

        elif len(rank2) == 2:
            if v >= maior:
                maior = v
                rank2.insert(-1, item)
            elif v < menor:
                menor = v
                rank2.insert(0, item)
            elif v < maior and v >= menor:
                rank2.insert(1, item)

        elif len(rank2) == 3:
            if v >= maior:
                maior = v
                rank2.insert(-1, item)
            elif v < menor:
                menor = v
                rank2.insert(0, item)
            elif v == menor:
                rank2.insert(1, item)
            elif v < maior and v > menor:
                rank2.insert(2, item)

print('-=' * 25)
print(f'{"== RANKING DOS JOGADORES == ":^40}')
for pos, c in enumerate(rank2):
    for k , v in rank2[pos].items():
        print(f'{pos+1}º colocado foi {k}, com valor {v}. ')

