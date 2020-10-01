info = {'Dia': '', 'Mês': '', 'Ano': ''}
info['Dia'] = int(input('Em que dia você nasceu? '))
info['Mês'] = str(input('Qual o mês de nascimento? '))
info['Ano'] = int(input('Qual o ano do seu nascimento? '))
for k, v in info.items():
    print(f'{k} de nascimento é {v}, ', end='')
print(f'\nVocê nasceu em {info["Dia"]}/{info["Mês"]}/{info["Ano"]}')
