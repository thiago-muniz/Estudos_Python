
regiões = ('Sudeste', 'Sul', 'Norte', 'Nordeste', 'Centro-Oeste')
sudeste = (('Rio de Janeiro', 'Rio de Janeiro', 'RJ', (21, 22, 24)),
        ('São Paulo', 'São Paulo', 'SP', (11, 12, 13, 14, 15, 16, 17, 18, 19)),
        ('Minas Gerais', 'Belo Horizonte', 'BH', (31, 32, 33, 34, 35, 37, 38)),
        ('Espírito Santo', 'Vitória', 'ES', (27, 28)))

sul = (('Paraná', 'Curitiba', 'PR', (41, 42, 43, 44, 45, 46)),
       ('Rio Grande do Sul', 'Porto Alegre', 'RS', (51, 53, 54, 55)),
       ('Santa Catarina', 'Florianópolis', 'SC', (47, 48, 49)))

centrooeste = (('Goiás', 'Goiânia', 'GO', (62, 64)),
               ('Mato Grosso', 'Cuiabá', 'MT', (65, 66)),
               ('Mato Grosso do Sul', 'Campo Grande', 'MS', 67),
               ('Distrito Federal', 'Brasília', 'DF', 61))

nordeste = (('Alagoas', 'Maceió', 'AL', 82),
            ('Bahia', 'Salvador', 'BA', (71, 73, 74, 75, 77)),
            ('Ceará', 'Fortaleza', 'CE', (85, 88)),
            ('Maranhão', 'São Luiz', 'MA', (98, 99)),
            ('Paraíba', 'João Pessoa', 'PB', 83),
            ('Pernambuco', 'Recife', 'PE', (81, 87)),
            ('Piauí', 'Terezina', 'PI', (86, 89)),
            ('Rio Grande do Norte', 'Natal', 'RN', 84),
            ('Sergipe', 'Aracajú', 'SE', 79))

norte = (('Acre', 'Rio Branco', 'AC', (21, 22, 24)),
         ('Amapá', 'Macapá', 'AP', (21, 22, 24)),
         ('Amazonas', 'Manaus', 'MA', (21, 22, 24)),
         ('Pará', 'Belém', 'PA', (21, 22, 24)),
         ('Rondônia', 'Porto Velho', 'RO', (21, 22, 24)),
         ('Roraima', 'Boa Vista', 'RR', (21, 22, 24)),
         ('Tocantins', 'Palmas', 'TO', (63)))
brasil = (sul[:], sudeste[:], norte[:], centrooeste[:], nordeste[:])
numeroestados = len(sul) + len(sudeste) + len(norte) + len(nordeste) + len(centrooeste)
print('-=' * 30)
print(f'{"INFO BRASIL": ^60}')
print('-=' * 30)
print(f'Ao todo o Brasil possuí {numeroestados-1} estados e o Distrito Federal')

while True:
    regiao = int(input('Escolha uma Região do Brasil: \n'
                       '[0] Sudeste \n'
                       '[1] Sul \n'
                       '[2] Norte \n'
                       '[3] Nordeste \n'
                       '[4] Centro Oeste \n'))
#SUDESTE
    if regiao == 0:
        print(f'Estes são os estados da região {regiões[regiao]}:')
        for pos, estados in enumerate(sudeste):
            print(f'[{pos}] - {estados[0]} ')
        estadoescolha = int(input('Escolha um estado: '))
        for pos, estados in enumerate(sudeste):
            if estadoescolha == pos:
                print('-=' * 30)
                print(f'A capital de {sudeste[pos][0]} é {sudeste[pos][1]}')
                print(f'A sigla do estado é {sudeste[pos][2]} e o código de região é {sudeste[pos][3]}')
                print('-=' * 30)
        while True:
            continuar = str(input('Deseja continuar? [ S / N ]')).upper().strip()
            if continuar == 'S':
                break
            elif continuar == 'N':
                break
            else:
                print('Opção inválida!')
        if continuar == 'N':
            break
#SUL
    elif regiao == 1:
        print(f'Estes são os estados da região {regiões[regiao]}')
        for pos, estados in enumerate(sul):
            print(f'[{pos}] - {estados[0]} ')
        estadoescolha = int(input('Escolha um estado: '))
        for pos, estados in enumerate(sul):
            if estadoescolha == pos:
                print('-=' * 30)
                print(f'A capital de {sul[pos][0]} é {sul[pos][1]}')
                print(f'A sigla do estado é {sul[pos][2]} e o código de região é {sul[pos][3]}')
                print('-=' * 30)
        while True:
            continuar = str(input('Deseja continuar? [ S / N ]')).upper().strip()
            if continuar == 'S':
                break
            elif continuar == 'N':
                break
            else:
                print('Opção inválida!')
        if continuar == 'N':
            break
#NORTE
    elif regiao == 2:
        print(f'Estes são os estados da região {regiões[regiao]}')
        for pos, estados in enumerate(norte):
            print(f'[{pos}] - {estados[0]} ')
        estadoescolha = int(input('Escolha um estado: '))
        for pos, estados in enumerate(norte):
            if estadoescolha == pos:
                print('-=' * 30)
                print(f'A capital de {norte[pos][0]} é {norte[pos][1]}')
                print(f'A sigla do estado é {norte[pos][2]} e o código de região é {norte[pos][3]}')
                print('-=' * 30)
        while True:
            continuar = str(input('Deseja continuar? [ S / N ]')).upper().strip()
            if continuar == 'S':
                break
            elif continuar == 'N':
                break
            else:
                print('Opção inválida!')
        if continuar == 'N':
            break
#NORDESTE
    elif regiao == 3:
        print(f'Estes são os estados da região {regiões[regiao]}')
        for pos, estados in enumerate(nordeste):
            print(f'[{pos}] - {estados[0]} ')
        estadoescolha = int(input('Escolha um estado: '))
        for pos, estados in enumerate(nordeste):
            if estadoescolha == pos:
                print('-=' * 30)
                print(f'A capital de {nordeste[pos][0]} é {nordeste[pos][1]}')
                print(f'A sigla do estado é {nordeste[pos][2]} e o código de região é {nordeste[pos][3]}')
                print('-=' * 30)
        while True:
            continuar = str(input('Deseja continuar? [ S / N ]')).upper().strip()
            if continuar == 'S':
                break
            elif continuar == 'N':
                break
            else:
                print('Opção inválida!')
        if continuar == 'N':
            break
#CENTRO OESTE
    elif regiao == 4:
        print(f'Estes são os estados da região {regiões[regiao]}')
        for pos, estados in enumerate(centrooeste):
            print(f'[{pos}] - {estados[0]} ')
        estadoescolha = int(input('Escolha um estado: '))
        for pos, estados in enumerate(centrooeste):
            if estadoescolha == pos:
                print('-=' * 30)
                print(f'A capital de {centrooeste[pos][0]} é {centrooeste[pos][1]}')
                print(f'A sigla do estado é {centrooeste[pos][2]} e o código de região é {centrooeste[pos][3]}')
                print('-=' * 30)
        while True:
            continuar = str(input('Deseja continuar? [ S / N ]')).upper().strip()
            if continuar == 'S':
                break
            elif continuar == 'N':
                break
            else:
                print('Opção inválida!')
        if continuar == 'N':
            break
print('-=' * 30)
print('Obrigado por utilziar o programa!')
print('-=' * 30)
