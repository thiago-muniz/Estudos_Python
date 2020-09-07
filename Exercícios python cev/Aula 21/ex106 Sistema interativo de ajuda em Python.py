'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''
def painel(txt):
    print(f'\033[0;30;46m{"-"}' * 30)
    print(f'{txt:^30}')
    print(f'\033[0;30;46m{"-"}' * 30)
    print('\033[m')


def interactivehelp(txt):
    from time import sleep
    painel(f'Acessando o Manual do comando {txt}')
    sleep(2)
    print(f'\033[0;37;40m')
    help(txt)
    print(f'\033[m')


#programa principal
while True:
    painel('SISTEMA DE AJUDA PyHelp')
    funçao = str(input('Nome da Função ou Biblioteca desejada: ')).strip().lower()
    if funçao == 'fim':
        painel('ATÉ LOGO!')
        break
    else:
        interactivehelp(funçao)
