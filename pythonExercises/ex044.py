preco = float(input('Digite o preço do produto: '))
forma = input('Digite a forma de pagamento: ')
dinheiro = 'R${:.2f}'.format(preco - (preco * 0.10))
avista = 'R${:.2f}'.format(preco - (preco * 0.05))
ate2x = 'R${:.2f}'.format(preco)
maisde2x = 'R${:.2f}'.format(preco + (preco * 0.20))
if forma == 'dinheiro' or 'cheque':
    print(dinheiro)
elif forma == 'cartão':
    print(avista)
elif forma == '2x' or forma == '1x':
    print(ate2x)
elif forma == '3x ou mais':
    print(maisde2x)