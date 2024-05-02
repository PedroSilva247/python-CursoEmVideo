import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n1 = random.randint(0, 5)
n2 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if n1 == n2:
    print('PARABÉNS! Você adivinhou!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n1, n2))