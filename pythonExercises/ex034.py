salario = float(input('Digite seu salário: '))
if salario > 1250:
    salau = salario + (salario * 0.10)
    au = '10%'
else:
    salau = salario + (salario * 0.15)
    au = '15%'
print('Seu salario antes era R${:.2f} agora é R${:.2f}. Você teve um aumento de {}!'.format(salario, salau, au))