maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    if 2023 - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Maiores de idade: {}'.format(maior))
print('Menores de idade: {}'.format(menor))