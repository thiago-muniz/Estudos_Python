'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
'''
jogador = dict()
jogadortemp = dict()
gols = list()
golstemp = list()
time = list()

while True:
    jogadortemp['Nome'] = str(input('Nome do Jogador: '))
    jogadortemp['Partidas'] = int(input(f'Quantas partidas jogou {jogadortemp["Nome"]}? '))
    soma = 0
    for n in range(1, jogadortemp['Partidas']+1):
        gol = int(input(f'Quantos gols {jogadortemp["Nome"]} fez na {n}ª partida? '))
        gols.append(gol)
        soma += gol
    jogadortemp['Gols'] = gols[:]
    jogadortemp['Total'] = soma
    jogador = jogadortemp.copy()
    time.append(jogador)

    while True:
        continuar = str(input('Continuar? [S/N]')).upper().strip()
        if continuar in 'SN':
            gols.clear()
            break
        else:
            print('Valor não permitido.')
    if continuar == 'N':
        break
print('=-' * 30)
print(f'Cód {"Nome":<10}{"Gols"}     {"Total":>}')
for cod, j in enumerate(time):
    print(f'{cod:<4}{j["Nome"]:<10}{j["Gols"]}     {j["Total"]:<}')

print('=-' * 30)
while True:
    mostrardados = int(input('Mostrar dados de qual Jogador? (999 para parar) '))
    if mostrardados == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {time[mostrardados]["Nome"]}')
    for partida, j in enumerate(time[mostrardados]['Gols']):
        print(f'No jogo {partida+1} fez {j} gols')
print('<< VOLTE SEMPRE >>')

