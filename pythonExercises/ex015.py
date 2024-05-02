d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pd = d * 60
pkm = km * 0.15
pt = pd + pkm
print('O total a pagar é de R${:.2f}'.format(pt))