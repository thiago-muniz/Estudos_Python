def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res


def moeda(preço):
    res = str(f'{preço:.2f}')
    if '.' in res:
        res = res.replace('.', ',')
    return f'R${res}'
