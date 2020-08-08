'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
listaimpar = []
listapar = []
lista = [listapar,listaimpar]

for c in range(0,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        listapar.append(num)
    if num % 2 == 1:
        listaimpar.append(num)

listapar.sort()
listaimpar.sort()
print(f'A lista de números pares em ordem crescente: {listapar}')
print(f'A lista de números ímpares em ordem crescente: {listaimpar}')