si = 0
hv = ''
mme21 = 0
ihv = 0
for c in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: ').lower()
    print(40*'-')
    si += idade
    if sexo == 'masculino' and idade > ihv:
        ihv = idade
        hv = nome
    if sexo == 'feminino' and idade < 21:
        mme21 += 1
m = si / 4
print('A média das idades é {} anos'.format(m))
print('O nome do homem mais velho é {} com {} anos'.format(hv, ihv))
print('Há {} mulher(es) com menos de 21 anos'.format(mme21))