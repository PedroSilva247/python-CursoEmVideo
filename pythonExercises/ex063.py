n = int(input('Digite um número inteiro: '))
a = 0
u = 0
pn = 0
i = 1
if n <= 0:
    print()
elif n == 1:
    print(0)
elif n == 2:
    print(0)
    print(1)
else:
    print(0)
    pn = 0
    print(1)
    u = 1
    while i < n-1:
        a = pn + u
        print(a)
        pn = u
        u = a
        i += 1
