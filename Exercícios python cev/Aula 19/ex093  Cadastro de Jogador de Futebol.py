'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''
infojogador = dict()
gols = list()

infojogador['Nome'] = str(input('Nome do Jogador: '))
infojogador['Partidas'] = int(input(f'Quantas partidas jogou {infojogador["Nome"]}? '))

for n in range(1, infojogador['Partidas']+1):
    gol = int(input(f'Quantos gols {infojogador["Nome"]} fez na {n}ª partida? '))
    gols.append(gol)

infojogador['Gols'] = gols
print('-=' * 30)
print(infojogador)
print('-=' * 30)
for k, v in infojogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {infojogador["Nome"]} jogou {len(gols)} partidas.')
for pos, n in enumerate(gols):
    print(f'{f"=> Na {pos+1}ª partida , fez {n:>2} gols.":>32}')
    n += n
print(f'Foi um total de {n} gols.')