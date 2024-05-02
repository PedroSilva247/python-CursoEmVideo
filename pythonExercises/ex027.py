nome = input('Digite seu nome completo: ')
nomes = nome.split()
pnome = nomes[0]
unome = nomes[len(nomes)-1]
print(nome)
print('Primeiro: {}'.format(pnome))
print('Último: {}'.format(unome))