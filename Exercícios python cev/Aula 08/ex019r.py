def sorteador(lista):
    from random import choice
    from time import sleep
    print('O aluno a apagar o quadro será...')
    sleep(3)
    print(choice(lista))


nomes = []
for i in range(1, 5):
    nomes.append(str(input(f'Nome do aluno {i}:')))
sorteador(nomes)
