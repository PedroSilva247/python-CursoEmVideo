n1 = int(input('Digite um número inteiro: '))
np = 0
for c in range(2, n1):
    if n1 % c == 0:
        np = 1

if np == 1:
    print('Esse número não é primo')
else:
    print('Esse número é primo')