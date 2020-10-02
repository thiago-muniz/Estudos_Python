def tipoDado(dado):
    '''
    Mostra informações sobre o tipo de dado fornecido pelo usuário.
    :param dado: dado inserido pelo usuário e armazenado em uma variável
    :return: retorna os valores do dicionario que contem informações sobre o dado
    '''
    dicio = {' é numérico? ': dado.isnumeric(), ' é alfanumérico? ': dado.isalnum(),
             ' é alfabético? ': dado.isalpha(), ' está escrito em minúsculo? ': dado.islower(),
             ' está escrito em maiúsculo? ': dado.isupper(), ' tem a primeira letra maiúscula? ': dado.istitle(),
            }
    print(f'-{dado}- é um dado do tipo ', type(dado))
    for k, v in dicio.items():
        if v == True:
            v = 'Sim'
        else:
            v = 'Não'
        print(f'-{dado}-{k}{v}')


#Programa Principal
dado = str(input('Digite algo: '))
tipoDado(dado)
