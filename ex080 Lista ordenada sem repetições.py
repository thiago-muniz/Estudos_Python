'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso mostre:
a) Quantos números foram digitados
b) A lista ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista
'''
lista = []
while True:
    lista.append(int(input('Digite um número: ')))

print(lista)

