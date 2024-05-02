import random
rand = random.randint(1, 3)
jogador = input('Pedra, papel ou tesoura? ')

if rand == 1:
    computador = 'pedra'
elif rand == 2:
    computador = 'papel'
elif rand == 3:
    computador = 'tesoura'
print()
print('Jogador: {}'.format(jogador))
print('Computador: {}'.format(computador))
print()
if computador == jogador:
    print('Empatamos!')
elif computador == 'pedra' and jogador == 'tesoura' or computador == 'tesoura' and jogador == 'papel' or computador == 'papel' and jogador == 'pedra':
    print('Eu ganhei de você!')
elif jogador == 'pedra' and computador == 'tesoura' or jogador == 'tesoura' and computador == 'papel' or jogador == 'papel' and computador == 'pedra':
    print('Parabéns! Você venceu!')