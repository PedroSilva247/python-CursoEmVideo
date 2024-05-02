dist = float(input('Digite qual é a distância da viagem em Km: '))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print('Preço da passagem: R${:.2f}'.format(preco))