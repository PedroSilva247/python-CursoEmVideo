n = 0
while True:
    n = int(input('Digite um numero (numero negativo para parar): '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n * c}')
    print(25*'-')
