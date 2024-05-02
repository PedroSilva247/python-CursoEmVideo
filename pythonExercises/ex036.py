valcasa = float(input('Valor do imóvel: '))
salario = float(input('Renda mensal: '))
tempo = int(input('Em quntos anos deseja pagar: '))

prestacao = valcasa / (tempo * 12)

if prestacao > salario * 0.3:
    print('Infelizmente seu emprestimo foi NEGADO!')
else:
    print('Seu emprestimo foi ACEITO!')