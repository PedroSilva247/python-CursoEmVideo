n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('REPROVADO!')
elif m < 7 and m > 5:
    print('RECUPERAÇÃO!')
elif m >= 7:
    print('APROVADO!')
