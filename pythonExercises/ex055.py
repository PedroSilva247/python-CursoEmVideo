peso = float(input('Digite seu peso: '))
maior = peso
menor = peso
for c in range(0, 4):
    peso = float(input('Digite seu peso: '))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))