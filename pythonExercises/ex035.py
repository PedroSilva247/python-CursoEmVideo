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
    print('É possivel formar um triangulo com essas retas')
else:
    print('Não é possivel formar um triangulo com essas retas')