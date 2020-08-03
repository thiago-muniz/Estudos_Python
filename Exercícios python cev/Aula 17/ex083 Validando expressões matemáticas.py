'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar ser a expressão passada está com os parênteses abertos
e fechados na ordem correta.
'''
expressao = str(input('Digite uma expressão com parênteses: '))
pilha = list()
for parenteses in expressao:
    if '(' in expressao:
        pilha.append('(')
    elif ')' in expressao:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('sua expressão está certa!')
else:
    print('Sua expressão está errada!')
print(lista)
