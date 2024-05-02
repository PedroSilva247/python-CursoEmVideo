frase = input('Digite um a frase: ')
fse = ''.join(frase.split())
i = int(len(fse)) - 1
frasein = ''
for c in range(0, len(fse)):
    frasein += str(fse[i])
    i -= 1
if str(fse.lower()) == str(frasein.lower()):
    print('A frase {} é um palíndromo'.format(frase.upper()))
else:
    print('A frase {} não é um palíndromo'.format(frase.upper()))