n1 = float(input('Digite o valor da primeira reta: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceira reta: '))

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

retasmen = n1 + n2 + n3 - mai

if retasmen > mai:
    if n1 == n2 == n3:
        tipo = 'EQUILÁTERO'
    elif n1 == n2 or n2 == n3 or n1 == n3:
        tipo = 'ISÓCELES'
    elif n1 != n2 and n2 != n3 and n1 != n3:
        tipo = 'ESCALENO'
    print('É possivel formar um triangulo {} com essas retas'.format(tipo))
else:
    print('Não é possivel formar um triangulo com essas retas')
