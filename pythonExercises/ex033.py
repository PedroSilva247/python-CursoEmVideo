n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2:
    if n1 > n3:
        mai = n1
    else:
        mai = n3
else:
    if n2 > n3:
        mai = n2
    else:
        mai = n3

if n1 < n2:
    if n1 < n3:
        men = n1
    else:
        men = n3
else:
    if n2 < n3:
        men = n2
    else:
        men = n3

print('O menor numero é {}'.format(men))
print('O maior número é {}'.format(mai))