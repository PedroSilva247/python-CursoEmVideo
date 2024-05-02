a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B : {b}')
# dessa forma nao é criada uma copia, e sim uma ligação entre as listas
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B : {b}')
# dessa forma é criada uma copia, e não uma ligação entre as listas