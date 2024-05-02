import random
t = 1
computador = random.randint(0, 10)
jogador = int(input('Pensei em um numero de 0 a 10, tente adivinhar: '))
while computador != jogador:
    print(50*'-')
    jogador = int(input('Você errou, tente novamente: '))
    t += 1
print(25*'-*')
print('Parabens, você acertou em {} tentativas!'.format(t))
