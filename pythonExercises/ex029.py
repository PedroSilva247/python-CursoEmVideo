vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você ultrapassou o limite de velocidade de 80Km/h, e agora deverá pagar uma multa de R${:.2f}.'.format(multa))
print('Bom dia! Dirija com segurança!')