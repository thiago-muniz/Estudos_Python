biblioteca = []
livro = {}
for c in range(0, 2):
    livro['título'] = str(input('Título do Livro: '))
    livro['ano'] = int(input('Ano de lançamento: '))
    livro['autor'] = str(input('Autor: '))
    biblioteca.append(livro.copy())
print(biblioteca)