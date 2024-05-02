n = int(input('Valor a ser sacado: '))

n50 = n // 50
n %= 50
n20 = n // 20
n %= 20
n10 = n // 10
n %= 10
n1 = n // 1
n %= 1

print(f'''
Notas de 50: {n50}
Notas de 20: {n20}
Notas de 10: {n10}
Notas de 1: {n1}''')