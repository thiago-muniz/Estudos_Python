'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
lista = []
listaflu = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
jogos = int(input('Quantos jogos deseja fazer?'))
for c in range(1, jogos+1): # quantos jogos
    for c in range(0,6): # números por jogo
        num = randint(1, 60)
        listaflu.append(num)
        if num in lista == num:
            num = randint(1, 60)
            listaflu.append(num)
    lista.append(listaflu[:])
    listaflu.clear()

for p, c in enumerate(lista):
    print(f'Jogo {p+1}: ',end=' ')
    print(lista[p])