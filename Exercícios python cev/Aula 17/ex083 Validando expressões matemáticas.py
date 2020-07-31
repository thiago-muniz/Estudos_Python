'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar ser a expressão passada está com os parênteses abertos
e fechados na ordem correta.
'''
lista = str(input('Digite uma expressão com parênteses: '))
lista.split()
if '('and')' in lista :                             #Primeira avaliação - se tem  '(' e ')' na lista
    if lista.count('(') == lista.count(')'):        #Segunda avaliação - se tem em pares os elementos
        if lista.find('(') > lista.find(')'):       #Terceira avalaiação - se a primeira ocorrencia de ')' acontece antes de '(' esta errado
            print('Sua lista está errada!')
        else:
            print('4 análise')                      #Quarta avaliação -
            for n in range(0, len(lista)):
                if lista[n] == '(':
                print(lista[n])
    else:
        print('Sua Expressão está errada!')
else:
    print('Sua Expressão está errada!')


print(lista)
