p18 = 0
h = 0
m20 = 0
while True:
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: '))
    s = s.upper()
    if i > 18:
        p18 += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        m20 += 1
    c = input('Quer continuar [S/N]? ')
    print(25*'-')
    if c.upper() == 'N':
        break
print(f'{p18} pessoas tem mais de 18 anos')
print(f'{h} homens foram cadastrados')
print(f'{m20} mulheres com mais de 20 anos foram cadastradas')


