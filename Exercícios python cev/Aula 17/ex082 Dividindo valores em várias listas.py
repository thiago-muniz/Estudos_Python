'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = list()
listapar = list()
listaimpar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    while True:
        c = str(input('Deseja continuar? [ S / N ]')).upper().strip()
        if c == 'S' or c == 'N':
            break
        else:
            print('Opção incorreta! Digite "S" ou "N"')

    if c == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista de números pares é {listapar}')
print(f'A lista de números ímpares é {listaimpar}')