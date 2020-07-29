'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso mostre:
a) Quantos números foram digitados
b) A lista ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista
'''
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continua = ''
    while True:
        continua = str(input('Deseja adicionar mais um número? ')).upper().strip()
        if continua == 'S' or continua == 'N':
            break
        else:
            print('valor inválido.')
    if continua == 'N':
        break

print('-=' * 30)
print(f'Foram digitados {len(lista)} valores')
print(f'A lista em forma decrescente é: ', end='')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')

