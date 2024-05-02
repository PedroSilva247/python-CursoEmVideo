n1 = int(input('Digite um número para descobrir seu fatorial: '))
i = n1
f = 1
while i > 0:
    f *= i
    i -= 1
print(f)