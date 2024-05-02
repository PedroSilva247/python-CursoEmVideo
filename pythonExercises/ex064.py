n = 0
s = 0
qn = 0
while n != 999:
    n = int(input('Digite um número (digite 999 para parar o programa): '))
    s += n
    qn += 1
s -= 999
qn -= 1
print('Você digitou {} números e a soma entre eles é {}'.format(qn, s))
