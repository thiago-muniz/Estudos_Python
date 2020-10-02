lista = ['Antecessor', 1, 'Número digitado', 1, 'Sucessor', 1]
lista[3] = int(input('Digite um número: '))
lista[1] = lista[3] - 1
lista[5] = lista[3] + 1
print(f'{lista[2]} foi {lista[3]}')
print(f'Seu {lista[0]} é igual a {lista[1]}')
print(f'Seu {lista[4]} é igual a {lista[5]}')

