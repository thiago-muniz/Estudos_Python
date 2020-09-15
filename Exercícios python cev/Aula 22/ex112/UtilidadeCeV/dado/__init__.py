def leiaDinheiro(msg):
    válido = False
    while not válido:
        p = str(input(msg)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'Erro: {p} é um preço inválido.')
        else:
            válido = True
            return float(p)


