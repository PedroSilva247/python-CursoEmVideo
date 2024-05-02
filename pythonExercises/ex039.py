ano = int(input('Digite seu ano de nascimento: '))
idade = 2023 - ano
if idade == 18:
    print('Já é hora de você se alistar!')
elif ano > 2023:
    print('Digite um ano anterior a 2023')
elif idade > 18:
    print('Já fazem {} anos que você se alistou.'.format(idade - 18))
elif idade < 18:
    print('Da que {} anos você terá que se alistar'.format(18 - idade))
