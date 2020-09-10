def aumentar(preço, taxa, fmoeda=True):
    res = preço + (preço * taxa/100)
    if fmoeda == True:
        return moeda(res)
    return res


def diminuir(preço, taxa, fmoeda=False):
    res = preço - (preço * taxa/100)
    if fmoeda == True:
        return moeda(res)
    return res


def dobro(preço, fmoeda=False):
    res = preço * 2
    if fmoeda == True:
        return moeda(res)
    return res


def metade(preço, fmoeda=False):
    res = preço / 2
    if fmoeda == True:
        return moeda(res)
    return res


def moeda(preço):
    res = str(f'{preço:.2f}')
    if '.' in res:
        res = res.replace('.', ',')
    return f'R${res}'
