peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Seu imc é {:.2f}. Abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é {:.2f}. Peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é {:.2f}. Sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc é {:.2f}. Obesidade!'.format(imc))
elif imc >= 40:
    print('Seu imc é {:.2f}. Obesidade mórbida!'.format(imc))