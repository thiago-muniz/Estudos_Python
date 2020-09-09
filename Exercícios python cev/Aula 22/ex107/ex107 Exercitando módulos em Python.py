'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
#Programa Principal
import moeda
valor = float(input('Digite um valor:R$ '))
print(f'O dobro de {valor} é {moeda.dobro(valor):.2f}')
print(f'A metade de {valor} é {moeda.metade(valor):.2f}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor):.2f}')
print(f'Diminuindo 10%, temos {moeda.diminuir(valor):.2f}')