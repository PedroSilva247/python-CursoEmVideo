lista = ['Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Livro', 30]
produtos = []
precos = []
for c in lista:
    if lista.index(c) % 2 == 0:
        produtos += [c]
    else:
        precos += [c]
print(40*'-')
print(f"{'LISTAGEM DE PREÇOS':^40}")
print(40*'-')
for c in produtos:
    print(end=''f"{c:.<30}")
    print(f'R$ {precos[produtos.index(c)]:>7.2f}')
print(40*'-')
