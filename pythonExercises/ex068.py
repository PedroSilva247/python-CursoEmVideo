import random
computador = random.randint(1, 10)
while True:
    n = int(input('Jogue um número: '))
    PouI = input('Escolha entre par ou ímpar [P/I]: ')
    s = n + computador
    r = 'P' if s % 2 == 0 else 'I'
    print(f'\nO computador escolheu {computador} e você escolheu {n}, totalizando {computador + n}.')
    if r.upper() == PouI.upper():
        print('Parabéns, você venceu!')
        print('\nVamos jogar novamente!')
        print(25*'-')
    else:
        print('O computador venceu!')
        break