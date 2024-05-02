produto = input('Produto: ')
preco = float(input('Preço: '))
m1000 = 0
mp = preco
pmp = produto
total = preco
if preco > 1000:
    m1000 += 1
addm = 'w'
while True:
    addm = input('Adicionar mais produtos [S/N]? ')
    if addm.lower() == 's' or addm.lower() == 'n':
        print(25*'-')
        break

while True:
    produto = input('Produto: ')
    preco = float(input('Preço: '))
    total += preco
    if preco < mp:
        pmp = produto
        mp = preco
    if preco > 1000:
        m1000 += 1

    while True:
        addm = input('Adicionar mais produtos [S/N]? ')
        if addm.lower() == 's' or addm.lower() == 'n':
            print(25 * '-')
            break
    if addm.lower() == 'n':
        break
print(f'Total: R${total:.2f}')
print(f'{m1000} produtos custam mais de R$1000.00')
print(f'O produto mais barato foi {pmp} que custa R${mp:.2f}')