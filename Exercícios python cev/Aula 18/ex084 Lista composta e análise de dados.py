'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
lista = list()
listageral = []
pesomai = pesomen = 0
listaleve = []
listapesado = []
r = ' '
nomepesado = 'erro'
nomeleve = ''
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    listageral.append(lista[:])
    lista.clear()
    while r != 'N':
        r = str(input('Deseja continuar? ')).upper().strip()
        if r == 'S':
            break
    if r == 'N':
        break
print(listageral)
for pos, indice in enumerate(listageral):
    if pos == 0:
        pesomai = pesomen = indice[1]
        nomepesado = nomeleve = indice[0]
        listaleve.append(indice)
        listapesado.append(indice)
    elif pos >= 1:
        if indice[1] >= pesomai:
            pesomai = indice[1]
            nomepesado = indice[0]
            if indice[1] > listapesado[0][1]:
                listapesado.pop()
            elif indice[1] == listapesado[0][1]:
                listapesado.append(indice)
        elif indice[1] <= pesomen:
            pesomen = indice[1]
            nomeleve = indice[0]
            if indice[1] < listaleve[0][1]:
                listaleve.pop()
                listaleve.append(indice)
            elif indice[1] == listaleve[0][1]:
                listaleve.append(indice)
            #como deixar a lista com um valor só quando a lista ja havia sido preenchida com duas listas?

print(f'Ao todo você cadastrou {len(listageral)} pessoas.')

print(f'O maior peso foi de {pesomai}Kg. Peso de: ', end='')
for pos, c in enumerate(listapesado):
    print(f'{listapesado[pos][0]}', end='  ')

print(f'\nO menor peso foi de {pesomen}Kg. Peso de: ', end='')
for pos, c in enumerate(listaleve):
    print(f'{listaleve[pos][0]}', end='  ')



