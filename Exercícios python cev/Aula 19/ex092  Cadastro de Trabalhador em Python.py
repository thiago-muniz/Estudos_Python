'''
Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
infotrabalhador = dict()
infotrabalhador['Nome'] = str(input('Nome: '))
anoatual = date.today().year
infotrabalhador['Idade'] = anoatual - int(input('Ano de Nascimento: '))
infotrabalhador['CTPS'] = int(input('Nº da Carteira de Trabalho?(0 - Nã o tem) '))
if infotrabalhador['CTPS'] > 0:
    infotrabalhador['Contratação'] = int(input('Ano da Contratação? '))
    infotrabalhador['Salário'] = float(input('Salário:R$ '))
    infotrabalhador['Aposentadoria'] = infotrabalhador['Contratação'] + 35

print('-='*30)
print(infotrabalhador)
for k, v in infotrabalhador.items():
    print(f'{k} tem valor {v}')
