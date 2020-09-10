def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço, aumento, redução):
    print('-' * 30)
    print(f'{"Reusmo do Valor":^30}')
    print('-' * 30)
    dicionario = {"Preço analizado:": moeda(preço),
             "Dobro do preço:": dobro(preço, True),
            "Metade do preço:":metade(preço, True),
                  f'{aumento}% de aumento:':aumentar(preço, aumento, True),
                  f'{redução}% de redução:':diminuir(preço, redução, True)}
    for k, v in dicionario.items():
        print(f'{k:<}    {v:>}')
    print('-' * 30)


