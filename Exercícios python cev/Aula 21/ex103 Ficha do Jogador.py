'''
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar a
ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(nome='', gols=''):
    '''
    Mostra ficha com nome e gols de um jogador
    :param nome: recebe o nome do jogador
    :param gols: recebe o número de gols do jogador
    :return: mostra ou não o nome o gols do jogador
    '''
    print('-' * 20)
    if nome == '':
        nome = '< Desconhecido >'
    if gols == '':
        gols = 0
    if nome and gols:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    elif gols and not nome:
        return f'O jogador {nome} fez {gols} gol(s)no campeonato.'
    elif nome and not gols:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    else:
        return f'O {nome} fez {gols} gols no campeonato.'


#Programa principal
name = str(input('Nome do jogador? '))
gol = str(input(f'Número de Gols de {name}: '))
print(ficha(name, gol))