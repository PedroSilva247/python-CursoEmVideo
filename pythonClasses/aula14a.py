n = 1
par = impar = t = 0
while n != 0:
    n = int(input('Digite um numero: '))
    t += 1
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Pares: {}\nImpares: {}\nTOTAL: {}'.format(par, impar, t))