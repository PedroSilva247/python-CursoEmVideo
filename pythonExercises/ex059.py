acao = 4
while acao != 5:
    print(40*'-')
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print()
    acao = int(input('''O que deseja fazer?
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
Digite: '''))
    if acao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    if acao == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    if acao == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
if acao == 5:
    print(22*'-')
    print('Você saiu do programa')
    print(22 * '-')
