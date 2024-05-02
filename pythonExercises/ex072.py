t = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {t[n].upper()}')
