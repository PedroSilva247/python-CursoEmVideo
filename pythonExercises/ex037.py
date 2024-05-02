n1 = int(input('Digite um número inteiro: '))
bc = input('Escolha entre BINÁRIO, OCTAL ou HEXADECIMAL: ')
if bc == 'binario':
    print('{} em binario é {}'.format(n1, bin(n1)))
elif bc == 'octal':
    print('{} em octal é {}'.format(n1, oct(n1)))
elif bc == 'hexadecimal':
    print('{} em hexadecimal é {}'.format(n1, hex(n1)))