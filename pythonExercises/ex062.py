pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
i = 0
qt = 1
while i <= 9:
    print(pt)
    pt += r
    i += 1
while qt != 0:
    i = 1
    qt = int(input('Deseja mostrar mais quantos termos: '))
    while i <= qt:
        print(pt)
        pt += r
        i += 1
print('Programa encerrado')